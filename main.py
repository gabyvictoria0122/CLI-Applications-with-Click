import click

@click.command()
@click.option("-n","--name", prompt="Enter your name", help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}!")

if __name__ == "__main__":
    hello()