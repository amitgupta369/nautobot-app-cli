import click
from .installer import (
    install,
    upgrade,
    uninstall,
    list_apps,
    list_installed,
    status
)


@click.group()
def cli():
    pass


@cli.command()
@click.argument("app_name")
@click.option("--ref", required=False)
def install_cmd(app_name, ref):
    install(app_name, ref)


@cli.command()
@click.argument("app_name")
def upgrade_cmd(app_name):
    upgrade(app_name)


@cli.command()
@click.argument("app_name")
def uninstall_cmd(app_name):
    uninstall(app_name)


@cli.command()
def list():
    list_apps()


@cli.command()
def list_installed():
    list_installed()


@cli.command()
@click.argument("app_name")
def status_cmd(app_name):
    status(app_name)


cli.add_command(install_cmd, name="install")
cli.add_command(upgrade_cmd, name="upgrade")
cli.add_command(uninstall_cmd, name="uninstall")
cli.add_command(status_cmd, name="status")