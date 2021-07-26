import click
from .craker import MD5Craker, abc

__all__ = ('attack',)

@click.command()
@click.argument('target')
@click.option('--max_len', type=int, help='Maximum password length', default=5)
@click.option('--chars', help='Password characters', default=abc)
def attack(target: str, max_len: int, chars: str):
    """Cracks hash from cli"""
    breaker = MD5Craker(target=target, max_len=max_len, chars=chars)
    pwd = breaker.attack()
    click.echo('Password: ' + pwd or 'Not Found')
