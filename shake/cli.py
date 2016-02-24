import click

@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version='0.0.1', prog_name='shake')
def cli():
    pass

@cli.command()
@click.argument('pkgs', nargs=-1)
def show(pkgs):
    """ Show info about a package """
    for pkg in pkgs:
        click.echo(pkg)

if __name__ == '__main__':
    cli()

