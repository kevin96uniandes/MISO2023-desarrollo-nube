from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/conversor'

db = SQLAlchemy(app)

from controllers import controllers
app.register_blueprint(controllers, url_prefix='/api')


