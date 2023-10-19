import pika

def insertar_cola(id):
    connection  = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue='archivos')
    channel.basic_publish(exchange='', routing_key='archivos', body=id)
    connection.close()
    print("Mensaje enviado: " + id)

def procesar_cola():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue='archivos')
    channel.basic_consume(on_message_callback=obtener_datos_cola, queue='archivos', auto_ack=True)
    print('Esperando mensajes...')
    channel.start_consuming()


def obtener_datos_cola(channel, method, properties, body):
    print("Mensaje recibido: %s" % body)
    