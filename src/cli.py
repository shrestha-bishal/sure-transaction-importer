import os
from dotenv import load_dotenv
import click
from src.commands.merge import run_merge

# load .env
load_dotenv()

@click.command()
@click.option("--merge", is_flag=True, help="Merge transaction files.")

def cli(merge):
    if merge:
        run_merge()
    if not any([merge]):
        click.echo("No action specified. Use --help for options.")

if __name__ == "__main__":
    cli()