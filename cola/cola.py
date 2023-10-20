from celery import Celery
import logging
from utils import FileUtils

celery_app = Celery('tasks', broker='redis://redis:6379/0')

fileUtils = FileUtils()

@celery_app.task(name='conversor')
def obtener_id_proceso(id):    
    
    logging.info("Iniciando app")   
    fileUtils.convertir_archivo(id)