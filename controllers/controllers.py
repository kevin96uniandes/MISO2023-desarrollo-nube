from flask import Blueprint, request, send_file
from modelos import EstadoArchivosSchema, Users, UsersSchema
import os
from utils import FileUtils
from repository.UserRepository import UserRepository
from celery import Celery
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_current_user, get_jwt
from flask import jsonify

controllers = Blueprint('controllers', __name__)

estado_archivo_schema = EstadoArchivosSchema()
users_schema = UsersSchema()
fileUtils = FileUtils()
userRepository = UserRepository()

celery_app = Celery('tasks', broker='redis://redis:6379/0')


@celery_app.task(name='conversor')
def obtener_id_proceso(id):
    pass


@controllers.route('/auth/signup', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password1 = data.get('password1')
    password2 = data.get('password2')

    if not email or not username or not password1 or not password2:
        return 'Los campos email, username y password son requeridos', 400

    if password1 != password2:
        return 'Las contraseñas deben ser iguales', 400

    stored_email = userRepository.obtener_por_email(email)

    if stored_email:
        return 'El email ya se encuentra en uso'
    else:
        if not fileUtils.validar_email(email):
            return 'Formato de email incorrecto'

    stored_username = userRepository.obtener_por_username(username)

    if stored_username:
        return 'El nombre de usuario ya se encuentra en uso'

    user = Users(
        username=username,
        email=email,
        password=generate_password_hash(password1)
    )

    userRepository.guardar_usuario(user)
    return users_schema.dump(user)

@controllers.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return 'Usuario y contraseña son obligatorios', 400

    stored_user = userRepository.obtener_por_username(username)
    if stored_user:
        if not check_password_hash(stored_user.password, password):
            return 'Credenciales incorrectas', 401
    else:
        return 'Credenciales incorrectas', 401
    token_de_acceso = create_access_token(identity=stored_user.id)
    return jsonify({"mensaje": "Inicio de sesión exitoso", "__token": token_de_acceso, "id": stored_user.id})


@controllers.route('/tasks', methods=['POST'])
@jwt_required()
def procesar_archivo(): 

    archivo = request.files['fileName']
    extension_convertir = request.form.get('newFormat')

    if archivo:
        nombre_del_archivo = archivo.filename
        extension_original = nombre_del_archivo.split('.')[-1]
        
        extension_original_minuscula = extension_original.lower()
        extension_convertir_minuscula = extension_convertir.lower()
        
        mensaje = fileUtils.validar_request(extension_original_minuscula, extension_convertir_minuscula)
        if mensaje == '':

            fileUtils.guardar_archivo_original(archivo)
            estado_archivo = fileUtils.crear_estado_documento(nombre_del_archivo, 'Ingresado', extension_original_minuscula, extension_convertir_minuscula)
            mensaje = {"id": estado_archivo.id}
            args = (estado_archivo.id, )
            obtener_id_proceso.apply_async(args)
        else:
            return mensaje, 400
    else:
        return "Debe enviar un archivo en el campo fileName", 400


    return estado_archivo_schema.dump(estado_archivo)

@controllers.route('/tasks/<int:id>', methods=['GET'])
@jwt_required()
def encontrar_archivo(id):
    estado = fileUtils.obtener_estado_tareas_por_id(id)
    if estado:
        if estado.estado == 'convertido':
            ruta_relativa = os.path.join('.', f'files/convertido')
            ruta_absoluta = os.path.abspath(ruta_relativa)

            archivo_convertido = os.path.join(ruta_absoluta, estado.nuevo_archivo)

            response = send_file(archivo_convertido, as_attachment=True)
            return response

        return estado_archivo_schema.dump(estado)
    else:
        return "Archivo no encontrado", 404

@controllers.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_tareas(id):  
    
        estado = fileUtils.obtener_estado_tareas_por_id(id)
        if estado:
            if estado.estado == 'convertido':
                fileUtils.eliminar_tarea(estado)
                return f"Tarea con el id {id} eliminada con exito",200
            else:
                return f"La tarea con id {id} se encuentra en estado {estado.estado}, debe esperar a que termine de procesar", 200
        else:
            return f"Tarea no encontrada con id {id}", 404

    
@controllers.route('/tasks', methods=['GET'])
@jwt_required()
def obtener_tareas():      
        data = request.get_json()

        max_value = data.get("max")
        order_value = data.get("order")
    
        tareas = fileUtils.obtener_lista_tareas_usuario('', max_value, order_value)
        return {"tareas": [estado_archivo_schema.dump(task) for task in tareas]}, 200
