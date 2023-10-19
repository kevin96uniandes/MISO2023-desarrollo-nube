from flask import Blueprint, request, send_file
from modelos import EstadoArchivosSchema
import os
from utils import FileUtils
from cola import procesar_cola, insertar_cola

controllers = Blueprint('controllers', __name__)

estado_archivo_schema = EstadoArchivosSchema()
fileUtils = FileUtils()

procesar_cola()

@controllers.route('/procesar', methods=['POST'])
def procesar_archivo(): 

    archivo = request.files['archivo']
    extension_convertir = request.form.get('extension_convertir')

    if archivo:
        nombre_del_archivo = archivo.filename
        print('nombre archivo')
        print(nombre_del_archivo.split('.')[0])
        extension_original = nombre_del_archivo.split('.')[-1]
        mensaje = fileUtils.validar_request(extension_original, extension_convertir)
        if mensaje == '':

            fileUtils.guardar_archivo_original(archivo)
            estado_archivo = fileUtils.crear_estado_documento(nombre_del_archivo, 'Ingresado', extension_original, extension_convertir)
            insertar_cola(estado_archivo.id)
        else:
            return mensaje, 400

    return estado_archivo_schema.dump(estado_archivo)

@controllers.route('/obtener-documento/<int:id>', methods=['GET'])
def encontrar_archivo(id):
    estado = fileUtils.obtener_estado_tareas_por_id(id)
    if estado:
        if estado.estado == 'convertido':
            ruta_relativa = os.path.join('.', 'files\convertido')
            ruta_absoluta = os.path.abspath(ruta_relativa)

            archivo_convertido = os.path.join(ruta_absoluta, estado.nombre_archivo)

            response = send_file(archivo_convertido, as_attachment=True)
            return response

        return estado_archivo_schema.dump(estado)
    else:
        return "Archivo no encontrado", 404