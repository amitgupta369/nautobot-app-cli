import subprocess
from .config import load_apps


PIP = "/opt/nautobot/bin/pip"

def resolve_source(app_name, ref=None, git=None, path=None):
    apps = load_apps()
    app = apps.get(app_name)

    if path:
        return path

    if git:
        return f"git+{git}@{ref}" if ref else f"git+{git}"

    repo = app["repo"]
    ref = ref or app["default_version"]

    return f"git+{repo}@{ref}"

def install(app_name, ref=None, git=None, path=None):
    source = resolve_source(app_name, ref, git, path)

    subprocess.run([
        PIP,
        "install",
        source
    ])

def upgrade(app_name, ref=None, git=None, path=None):
    source = resolve_source(app_name, ref, git, path)

    subprocess.run([
        PIP,
        "install",
        "--upgrade",
        source
    ])


def uninstall(app_name):
    apps = load_apps()
    app = apps[app_name]

    cmd = [
        PIP,
        "uninstall",
        "-y",
        app["package"]
    ]

    subprocess.run(cmd)


def list_apps():
    apps = load_apps()
    for app in apps:
        print(app)


def list_installed():
    subprocess.run([PIP, "list"])


def status(app_name):
    apps = load_apps()
    app = apps[app_name]

    subprocess.run([PIP, "show", app["package"]])