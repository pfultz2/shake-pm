import click
from shake.environment import load_env

@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version='0.0.1', prog_name='shake')
def cli():
    pass

def use_environment():
    def callback(ctx, param, value):
        if value is None: return load_env(value)
        else: return load_env('.')
    return click.option('-e', '--environment', envvar='SHAKE_ENV_DIR', callback=callback)

@cli.command()
@click.argument('pkgs', nargs=-1)
def show(pkgs):
    """ Show info about a package """
    for pkg in pkgs:
        click.echo(pkg)

@cli.command(name='list')
@use_environment()
@click.option('--installed', default=False, is_flag=True)
def list_command(environment, installed):
    """ List available packages """
    environment.load_channels()
    for pkg in environment.repo.list():
        click.echo(pkg)


if __name__ == '__main__':
    cli()

