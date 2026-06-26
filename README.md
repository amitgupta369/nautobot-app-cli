# Nautobot App CLI

Simple CLI to install, upgrade, uninstall, and manage Nautobot apps.

## Features

* Install apps from Git
* Install specific tag/branch/commit
* Upgrade apps
* Uninstall apps
* List available apps
* Check installed app status

---

## Recommended Installation (Option 1)

Install in separate virtual environment.

```bash
sudo mkdir -p /opt/nautobot-app-cli
sudo chown nautobo:nautobot /opt/nautobot-app-cli
git clone <your-repo> /opt/nautobot-app-cli
cd /opt/nautobot-app-cli
python3 -m venv venv
source venv/bin/activate
pip install .
```

Create global symlink:

```bash
sudo ln -s /opt/nautobot-app-cli/venv/bin/nautobot-app /usr/local/bin/nautobot-app
```

Validate:

```bash
nautobot-app --help
```

---

## Usage

List available apps:

```bash
nautobot-app list
```

Install default version:

```bash
nautobot-app install vlan-request
```

Supported Install command:

```bash
nautobot-app install vlan-request --ref v0.1.
nautobot-app install vlan-request
nautobot-app install vlan-request --ref v0.2.0
nautobot-app install vlan-request --git https://github.com/user/repo.git
nautobot-app install vlan-request --git https://github.com/user/repo.git --ref feature/dev
nautobot-app install vlan-request --path /tmp/nautobot-vlan-request
```

Upgrade command:

```bash
nautobot-app upgrade vlan-request
nautobot-app upgrade vlan-request --ref v0.2.0
nautobot-app upgrade vlan-request --git https://github.com/user/repo.git
nautobot-app upgrade vlan-request --git https://github.com/user/repo.git --ref main
nautobot-app upgrade vlan-request --path /tmp/nautobot-vlan-request
```

Uninstall app:

```bash
nautobot-app uninstall vlan-request
```

Check app status:

```bash
nautobot-app status vlan-request
```

List installed packages:

```bash
nautobot-app list-installed
```
