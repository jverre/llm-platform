import click

@click.group()
@click.option(
    "-v",
    "--verbose",
    count=True,
    default=0,
    help="-v for DEBUG",
)
def cli(verbose):
    print(verbose)

@cli.command("start")
@click.option(
    "--option1"
)
def start(option1):
    print('Will start server')

if __name__ == '__main__':
   cli()