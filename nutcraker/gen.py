import click
from .craker import MD5Craker

@click.command()
@click.argument('password')
def md5hash(password: str):
    """Generates the md5 hash for specified string"""
    click.echo(f'Hash for "{password}": {MD5Craker.md5(password)}')

if __name__ == '__main__':
    md5hash()
