import click
from flask import Flask

from flaskr import seeders


def register_commands(app: Flask):
    @app.cli.command("db:seed")
    def seed():
        """Seed the database with initial data."""
        click.echo("Seeding the database...")
        seeders.run()
        click.echo("Database seeded successfully.")