from celery import Celery
import logging
from configuracion import Config
from utils import FileUtils

celery_app = Celery('tasks', 
                    broker='redis://redis:6379/0')

@celery_app.task(name='conversor')
def obtener_id_proceso(id): 
    logging.info('creando contexto') 
    Config.init()
        
    logging.info('iniciando')
    fileUtils = FileUtils()
    fileUtils.procesar_elemento_cola(id)