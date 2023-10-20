from flask import Flask
from flask_cors import CORS
from modelos import db
app = Flask(__name__)

cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/conversor'

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

from controllers import controllers

app.register_blueprint(controllers, url_prefix='/api')






