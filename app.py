from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/conversor'

db = SQLAlchemy(app)

scheduler = BackgroundScheduler()

from controllers import controllers
from cola import procesar_cola

app.register_blueprint(controllers, url_prefix='/api')

scheduler.add_job(procesar_cola, 'interval', minutes=5)
scheduler.start()






