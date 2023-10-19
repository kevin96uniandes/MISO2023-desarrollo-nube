from celery import Celery


celery = Celery(__name__, broker='redis://localhost:6379/0')

@celery.task(name="convertir_archivo")
def convertir_archivo(id, nombre):
    from utils import FileUtils

    fileUtils = FileUtils()
    print(f"ejecutando cola con id {id}")

    try: 
        fileUtils.convertir_archivo(id)
    except:
        print(f"error a la hora de procesar la cola con id {id}")
