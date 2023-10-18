from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5433/conversor'

db = SQLAlchemy(app)


from controllers import controllers
app.register_blueprint(controllers, url_prefix='/api')


