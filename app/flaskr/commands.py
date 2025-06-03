import click
from flask import Flask

from flaskr import seeders
from flaskr import db


def register_commands(app: Flask):
    @app.cli.command("db:init")
    def init():
        """Initialize the database."""
        click.echo("Initializing the database...")
        with app.app_context():
            db.drop_all()
            db.create_all()
        click.echo("Database initialized successfully.")

    @app.cli.command("db:seed")
    def seed():
        """Seed the database with initial data."""
        click.echo("Seeding the database...")
        seeders.run()
        click.echo("Database seeded successfully.")
