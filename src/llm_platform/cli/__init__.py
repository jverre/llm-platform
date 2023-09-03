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
    # Start server
    import llm_platform.server as server
    import uvicorn
    uvicorn.run(server.app)

if __name__ == '__main__':
   cli()