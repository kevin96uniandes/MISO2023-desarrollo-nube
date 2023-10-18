from flask import Blueprint, request, send_file
from modelos import EstadoArchivosSchema,EstadoArchivos, db
import os

controllers = Blueprint('controllers', __name__)

estado_archivo_schema = EstadoArchivosSchema()

@controllers.route('/procesar', methods=['POST'])
def procesar_archivo():

    ruta_relativa = os.path.join('.', 'files\original')
    ruta_absoluta = os.path.abspath(ruta_relativa)


    archivo = request.files['archivo']
    extension_convertir = request.form.get('extension_convertir')

    if archivo:
        nombre_del_archivo = archivo.filename
        extension_original = nombre_del_archivo.split('.')[-1]


        print(ruta_absoluta)
        if not os.path.exists(ruta_absoluta):
            os.makedirs(ruta_absoluta)

        archivo_guardado = os.path.join(ruta_absoluta, archivo.filename)
        print(archivo_guardado)
        archivo.save(archivo_guardado)

        estado_archivos = EstadoArchivos(
            nombre_archivo=nombre_del_archivo,
            extension_original=extension_original,
            extension_nueva=extension_convertir,
            estado='En progreso'
        )

        db.session.add(estado_archivos)
        db.session.commit()

    return estado_archivo_schema.dump(estado_archivos)

@controllers.route('/obtener-documento/<int:id>', methods=['GET'])
def encontrar_archivo(id):
    estado = EstadoArchivos.query.get(id)
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