from flask import Flask
from flask_cors import CORS
from modelos import db
from configuracion import Config

app = Flask(__name__)

app = Config.init()
cors = CORS(app)

from controllers import controllers

app.register_blueprint(controllers, url_prefix='/api')






