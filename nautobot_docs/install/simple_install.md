cat /etc/os-release
sudo apt update && sudo apt upgrade

Install Python 3.13
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.13 python3.13-venv python3.13-dev
python3.13 --version

Install postgresql


sudo apt install curl ca-certificates
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
sudo apt update
sudo apt install postgresql-18 postgresql-contrib
sudo apt install build-essential python3-dev libpq-dev


sudo apt install git curl wget  libxml2-dev libxslt1-dev libffi-dev  libssl-dev zlib1g-dev 
sudo apt install redis-server  software-properties-common

sudo -u postgres psql
sudo useradd --system --create-home --shell /bin/bash nautobot
sudo mkdir -p /opt/nautobot
sudo chown nautobot:nautobot /opt/nautobot
sudo -iu nautobot


 python3.13 -m venv /opt/nautobot
 source /opt/nautobot/bin/activate
 pip install --upgrade pip wheel setuptools
 pip install nautobot
 nautobot-server init
 nano ~/.nautobot/nautobot_config.py
 nautobot-server generate_secret_key # It is throwing error need to investigate
# Set debug true to fix static issue nano ~/.nautobot/nautobot_config.py
nautobot-server migrate
nautobot-server createsuperuser
nautobot-server collectstatic --noinput
hostname -I

## Run Nautobot web 

```bash
nautobot-server runserver 0.0.0.0:8000
```


## Celery Worker Process
### Purpose
- Jobs
- Background Tasks
- Long-running Tasks

```bash
nautobot-server celery worker
```



## Celery beat (Scheduler)

### Purpose
- Scheduled Jobs
- Periodic Tasks

```bash
nautobot-server celery beat

```




