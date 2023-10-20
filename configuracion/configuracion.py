from flask import Flask
from modelos import db


class Config:

    @staticmethod
    def init():
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/conversor'

        app_context = app.app_context()
        app_context.push()

        db.init_app(app)
        db.create_all()
        return app