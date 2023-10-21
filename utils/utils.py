from moviepy.editor import VideoFileClip
from datetime import datetime
from modelos import EstadoArchivos, db
import os
import logging

class FileUtils:

    def procesar_elemento_cola(self, id):
        logging.info(f"ejecutando cola con id {id}")

        try: 
            estado_archivo = EstadoArchivos.query.get(id)
            self.editar_estado_documento(estado_archivo.id, 'procesando', '', datetime.now())
            
            nombre_archivo_convertido = f"{estado_archivo.id}_converted.{estado_archivo.extension_nueva}"

            if estado_archivo.extension_nueva == 'mp4':
                self.convertir_archivo(estado_archivo.nombre_archivo, nombre_archivo_convertido, 'libx264')
            if estado_archivo.extension_nueva == 'webm':
                self.convertir_archivo(estado_archivo.nombre_archivo, nombre_archivo_convertido, 'libvpx')
            if estado_archivo.extension_nueva == 'avi':
                self.convertir_archivo(estado_archivo.nombre_archivo, nombre_archivo_convertido, 'rawvideo')

            self.editar_estado_documento(estado_archivo.id, 'convertido', nombre_archivo_convertido,datetime.now())

            print(f"ejecutando cola con id {id} exitoso")

        except Exception as e:
            print(f"error a la hora de procesar la cola con id {id} {e}")
            self.editar_estado_documento(estado_archivo.id, 'fallido', '', datetime.now())


    def validar_request(self, extension_original, extension_convertir):
        if self.validar_extension_servicio_invalida(extension_original):
            return "el archivo adjunto no es valido, recuerda que debe ser mp4, webm o avi"
        if self.validar_extension_servicio_invalida(extension_convertir):
            return "la extensión ingresada para convertir no es valida, recuerda que debe ser mp4, webm o avi"
        if self.validar_extensiones_iguales(extension_original, extension_convertir):
            return "la extension del archivo ingresado y la extensión a compartir no deben ser las mismas"
        return ''

    def validar_extension_servicio_invalida(self, extension):
        if extension == 'mp4' or extension == 'webm' or extension == 'avi' :
            return False
        else:
            return True
        
    def validar_extensiones_iguales(self, extension_original, extension_convertir):
        if extension_original == extension_convertir:
            return True
        else:
            return False
        
    def guardar_archivo_original(self, archivo):
        ruta_relativa = os.path.join('.', 'files/original')
        ruta_absoluta = os.path.abspath(ruta_relativa)

        logging.info(ruta_absoluta)
        if not os.path.exists(ruta_absoluta):
           os.makedirs(ruta_absoluta)

        archivo_guardado = os.path.join(ruta_absoluta, archivo.filename)
        print(archivo_guardado)
        archivo.save(archivo_guardado)

    def convertir_archivo(self, nombre_archivo, nombre_archivo_convertido, code):
        ruta_relativa_original = os.path.join('.', 'files/original')
        ruta_absoluta_original = os.path.abspath(ruta_relativa_original)
        
        logging.info(ruta_absoluta_original)
        
        ruta_relativa_convertidos = os.path.join('.','files/convertido')
        ruta_absoluta_convertidos = os.path.abspath(ruta_relativa_convertidos)
        
        logging.info(ruta_absoluta_convertidos)
        
        if not os.path.exists(ruta_absoluta_convertidos):
           os.makedirs(ruta_absoluta_convertidos)

        ruta_absoluta_convertido = os.path.join(ruta_absoluta_convertidos, nombre_archivo_convertido)

        ruta_archivo_convertir = os.path.join(ruta_absoluta_original, nombre_archivo)      
        self.escribir_archivo_convertido(ruta_archivo_convertir, ruta_absoluta_convertido, code)      
        
    def escribir_archivo_convertido(self, ruta_archivo_convertir, ruta_absoluta_convertido, codec):
        video = VideoFileClip(ruta_archivo_convertir)
        video.write_videofile(ruta_absoluta_convertido, codec=codec)

    def crear_estado_documento(self, nombre_archivo, estado, extension_original, extension_convertir):
        estado_archivos = EstadoArchivos(
                nombre_archivo=nombre_archivo,
                extension_original=extension_original,
                extension_nueva=extension_convertir,
                estado=estado,
                nuevo_archivo='pending'
        )   

        db.session.add(estado_archivos)
        db.session.commit()

        return estado_archivos

    def editar_estado_documento(self, id, estado, nombre_archivo_convertido, fecha):

        estado_archivo = EstadoArchivos.query.get(id)
        estado_archivo.estado = estado
        estado_archivo.nuevo_archivo = nombre_archivo_convertido
        estado_archivo.fecha_procesamiento = fecha
        db.session.commit()

    def obtener_estado_tareas_por_id(self, id):
        return EstadoArchivos.query.get(id)
    
    def obtener_lista_tareas_usuario(self, id_user, max, order):
        query = db.session.query(EstadoArchivos)
        
        if order is not None:
            if order == 1:
                query = query.order_by(EstadoArchivos.id.asc())
            elif order == 0:
                query = query.order_by(EstadoArchivos.id.desc())
                
        if max is not None:
            query = query.limit(max)
            
                
        return query.all()
    
    def eliminar_tarea(self, estado):
        ruta_relativa_original = os.path.join('.', 'files/original')
        ruta_absoluta_original = os.path.abspath(ruta_relativa_original)
                
        ruta_archivo_original = os.path.join(ruta_absoluta_original, estado.nombre_archivo)    
                
        if os.path.exists(ruta_archivo_original):
            os.remove(ruta_archivo_original)
            logging.info(f"archivo {ruta_archivo_original} eliminado")        
                
        ruta_relativa_convertidos = os.path.join('.','files/convertido')
        ruta_absoluta_convertidos = os.path.abspath(ruta_relativa_convertidos)
        
        ruta_archivo_convertido = os.path.join(ruta_absoluta_convertidos, estado.nuevo_archivo)    
        
        if os.path.exists(ruta_archivo_convertido):
            os.remove(ruta_archivo_convertido)
            logging.info(f"archivo {ruta_archivo_convertido} eliminado")
            
        db.session.delete(estado)
        db.session.commit()                        
        
    
