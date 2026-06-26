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
