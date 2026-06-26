# Nautobot Production Installation (Ubuntu 22.04)

## Verify OS

```bash
cat /etc/os-release
sudo apt update && sudo apt upgrade -y
```

---

## Install Python 3.13

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.13 python3.13-venv python3.13-dev
python3.13 --version
```

---

## Install PostgreSQL

```bash
sudo apt install -y curl ca-certificates
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
sudo apt update
sudo apt install -y postgresql-18 postgresql-contrib
sudo apt install -y build-essential python3-dev libpq-dev
```

---

## Install Required Packages

```bash
sudo apt install -y git curl wget \
    libxml2-dev libxslt1-dev libffi-dev \
    libssl-dev zlib1g-dev \
    redis-server nginx software-properties-common
```

---

## Create Nautobot User

```bash
sudo useradd --system --create-home --shell /bin/bash nautobot
sudo mkdir -p /opt/nautobot
sudo chown nautobot:nautobot /opt/nautobot
sudo -iu nautobot
```

---

## Setup Nautobot Virtual Environment

```bash
python3.13 -m venv /opt/nautobot
source /opt/nautobot/bin/activate
pip install --upgrade pip wheel setuptools
pip install nautobot
```

---

## Initialize Nautobot

```bash
nautobot-server init
```

Update config:

```bash
nano ~/.nautobot/nautobot_config.py
```

Set:

```python
DEBUG = False
ALLOWED_HOSTS = ["*"]

CELERY_BROKER_URL = "redis://localhost:6379/0"
CACHEOPS_REDIS = "redis://localhost:6379/1"
```

Generate secret key:

```bash
nautobot-server generate_secret_key
```

Run:

```bash
nautobot-server migrate
nautobot-server createsuperuser
nautobot-server collectstatic --noinput
```

---

## Create Systemd Service (Web)

```bash
sudo nano /etc/systemd/system/nautobot.service
```

Add:

```ini
[Unit]
Description=Nautobot Web
After=network.target

[Service]
User=nautobot
Group=nautobot
WorkingDirectory=/opt/nautobot
ExecStart=/opt/nautobot/bin/gunicorn nautobot.core.wsgi:application --bind 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## Create Celery Worker Service

```bash
sudo nano /etc/systemd/system/nautobot-worker.service
```

Add:

```ini
[Unit]
Description=Nautobot Celery Worker
After=network.target

[Service]
User=nautobot
Group=nautobot
WorkingDirectory=/opt/nautobot
ExecStart=/opt/nautobot/bin/nautobot-server celery worker
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## Create Celery Beat Service

```bash
sudo nano /etc/systemd/system/nautobot-beat.service
```

Add:

```ini
[Unit]
Description=Nautobot Celery Beat
After=network.target

[Service]
User=nautobot
Group=nautobot
WorkingDirectory=/opt/nautobot
ExecStart=/opt/nautobot/bin/nautobot-server celery beat
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## Enable Services

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now nautobot
sudo systemctl enable --now nautobot-worker
sudo systemctl enable --now nautobot-beat
```

Check:

```bash
sudo systemctl status nautobot
sudo systemctl status nautobot-worker
sudo systemctl status nautobot-beat
```

---

## Configure Nginx

```bash
sudo nano /etc/nginx/sites-available/nautobot
```

Add:

```nginx
server {
    listen 80;
    server_name _;

    location /static/ {
        alias /home/nautobot/.nautobot/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Enable:

```bash
sudo ln -s /etc/nginx/sites-available/nautobot /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## Validate

```bash
redis-cli ping
nautobot-server check
nautobot-server celery inspect ping
hostname -I
```

Access:

```text
http://<server-ip>
```
