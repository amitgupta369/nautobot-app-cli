# Nautobot Deployment Approaches

This document explains the supported Nautobot deployment models and when to use them.

| # | Approach                                          | Type          | Best For                | Recommended             |
| - | ------------------------------------------------- | ------------- | ----------------------- | ----------------------- |
| 1 | Python venv + runserver                           | Native        | Development             | ⭐ Best for Dev          |
| 2 | Python venv + systemd + gunicorn + celery + nginx | Native        | Production              | ⭐ Best for Prod         |
| 3 | Docker Compose                                    | Container     | Dev / Test / Production | ⭐ Best container option |
| 4 | Helm Chart on Kubernetes                          | Orchestration | Enterprise Production   | ⭐ Best for Kubernetes   |

---

## 1. Python venv + runserver

Best for:

* Learning Nautobot
* Custom app development
* Debugging

Pros:

* Simple setup
* Fastest startup
* Easy debugging
* Live code changes

Cons:

* Not production safe
* No process supervision

Start:

```bash
source /opt/nautobot/bin/activate
nautobot-server runserver 0.0.0.0:8000
```

---

## 2. Python venv + systemd + gunicorn + celery + nginx

Best for:

* Production deployments
* Dedicated VMs
* Stable environments

Pros:

* Process supervision
* Auto restart
* Better performance
* Scalable
* Enterprise friendly

Cons:

* More setup required

Components:

```text
nginx
gunicorn
nautobot
celery worker
celery beat
postgres
redis
```

Recommended for long-running production.

---

## 3. Docker Compose

Best for:

* Quick full-stack deployment
* Development labs
* Testing
* Small production

Pros:

* Full stack in one file
* Easy setup
* Consistent environments
* Easy rebuild/reset

Cons:

* More moving parts than venv

Components:

```text
nautobot
postgres
redis
worker
beat
nginx
```

Start:

```bash
docker compose up -d
```

Recommended for portable deployments.

---

## 4. Helm Chart on Kubernetes

Best for:

* Enterprise production
* High availability
* Large-scale deployments

Pros:

* Standardized K8s deployment
* Easy upgrades
* Easy rollback
* Scaling support

Cons:

* Requires Kubernetes knowledge
* More operational complexity

Start:

```bash
helm install nautobot <chart>
```

Recommended for cloud-native production.

---

## Recommendation

| Environment     | Best Approach                       |
| --------------- | ----------------------------------- |
| Development     | Python venv + runserver             |
| Testing / UAT   | Docker Compose                      |
| Production      | systemd + gunicorn + celery + nginx |
| Enterprise / HA | Helm Chart on Kubernetes            |


This document explains supported operating systems, and recommended technology stack versions.

---

## Supported Operating Systems

| Operating System | Version   | Status    | Remarks                                |
| ---------------- | --------- | --------- | -------------------------------------- |
| Ubuntu           | 22.04 LTS | Supported | ⚠ Nearing EOL, plan upgrade            |
| Ubuntu           | 24.04 LTS | Supported | Recommended for new deployments        |
| RHEL             | 8.x       | Supported | Stable enterprise deployment           |
| RHEL             | 9.x       | Supported | Recommended for enterprise deployments |
| Amazon Linux     | 2023      | Supported | Recommended for AWS deployments        |

---

## Recommended Technology Stack

| Component      | Recommended Version | Remarks                    |
| -------------- |---------------------| -------------------------- |
| Python         | 3.13.x              | Recommended and stable     |
| Nautobot       | 3.1.x               | Current stable release     |
| PostgreSQL     | 18.x                | Recommended                |
| Redis          | 8.x                 | Recommended                |
| Gunicorn       | Latest stable       | Production web server      |
| Celery         | Latest stable       | Async job execution        |
| Nginx          | Latest stable       | Reverse proxy              |
| Docker         | 27+                 | Container deployments      |
| Docker Compose | v2                  | Container orchestration    |
| Kubernetes     | 1.30+               | Enterprise deployments     |
| Helm           | 3.x                 | Kubernetes package manager |
