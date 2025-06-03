import click
from flask.cli import with_appcontext
from app.models.database import init_db

def init_app(app):
    """Registrar comandos da linha de comando."""
    @app.cli.command('init-db')
    @with_appcontext
    def init_db_command():
        """Clear the existing data and create new tables."""
        init_db()
        click.echo('Initialized the database.')

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Inicializar o banco de dados."""
    init_db()
    click.echo('Banco de dados inicializado.') 