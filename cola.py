from controllers.healtcheckController import bluePrintHealthcheckController
from utils import FileUtils
from google.cloud import pubsub_v1
import json
import certifi
import logging
from flask_cors import CORS
from configuracion import Config

'''
celery_app = Celery('tasks', 
                    broker='redis://redis:6379/0')

@celery_app.task(name='conversor')
'''

NOMBRE_BUCKET = "video_format_converter_v2"
URL_BUCKET = "https://storage.googleapis.com/video_format_converter_v2/"
PROJECT_ID = "conversor-grupo-10-v2"
TOPIC_ID = "video_format_converter_topic_v2"
SUBSCRIPTION = "video_format_converter_topic_v2-sub"

def obtener_id_proceso(id):
    logging.info('creando contexto') 
    Config.init()
        
    logging.info('iniciando')
    fileUtils = FileUtils()
    fileUtils.procesar_elemento_cola(id)


subscriber = pubsub_v1.SubscriberClient()

# Forma el nombre completo de la suscripción
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION)

def callback(message):
    logging.info(f"Received message: {message.data}")
    # Decodifica los datos del mensaje (bytes) a una cadena
    message_data_str = message.data.decode('utf-8')

    # Analiza la cadena JSON para obtener el valor del campo "data"
    try:
        message_json = json.loads(message_data_str)
        data_value = message_json.get('id_video')
        # Puedes agregar aquí la lógica para procesar el mensaje
        obtener_id_proceso(data_value)
        logging.info(f"Received message with data: {data_value}")
        # Acknowledge the message para indicar que ha sido procesado
        message.ack()
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")



# Crea la suscripción
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
logging.info(f"Escuchando mensajes en la suscripción {subscription_path}")

app = Config.init()
cors = CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    # Espera a que la suscripción termine
    try:
        logging.info(f"Sacando de la suscripción")
        streaming_pull_future.result()
    except Exception as ex:
        logging.error(f"Error en la suscripción: {ex}")
        streaming_pull_future.cancel()

