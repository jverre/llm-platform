import click
import sqlite3

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
    # Configure sqlite3 platform
    conn = sqlite3.connect(".llm-platform/")
    c = conn.cursor()

    # Create empty tables
    c.execute('''
    CREATE TABLE IF NOT EXISTS models
    ([model_id] INTEGER PRIMARY KEY, [model_name] TEXT, [model_type] TEXT)
    ''')

    # c.execute('''
    # INSERT INTO models(model_id, model_name, model_type) 
    # SELECT 'openai_chat_completions', 'openai', 'openai')   
    # ''')
    
    conn.commit()

    # Start server
    import llm_platform.server as server
    import uvicorn
    uvicorn.run(server.app)

    print('start server')
    print('Will start server')

if __name__ == '__main__':
   cli()