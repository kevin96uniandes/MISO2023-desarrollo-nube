from moviepy.editor import VideoFileClip
from modelos import EstadoArchivos, db
import os
import logging

class FileUtils:

    def convertir_archivo(self, id):
        logging.info(f"ejecutando cola con id {id}")

        try: 
            estado_archivo = EstadoArchivos.query.get(id)
            self.editar_estado_documento(estado_archivo.id, 'procesando')

            if estado_archivo.extension_convertir == 'mp4':
                self.convertir_a_mp4(estado_archivo.nombre_del_archivo)
            if estado_archivo.extension_convertir == 'webm':
                self.convertir_a_webm(estado_archivo.nombre_del_archivo)
            if estado_archivo.extension_convertir == 'avi':
                self.convertir_a_avi(estado_archivo.nombre_del_archivo)

            self.editar_estado_documento(estado_archivo.id, 'convertido')

            print(f"ejecutando cola con id {id} exitoso")

        except Exception as e:
            print(f"error a la hora de procesar la cola con id {id}")
            self.editar_estado_documento(estado_archivo.id, 'fallido')


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

        print(ruta_absoluta)
        if not os.path.exists(ruta_absoluta):
           os.makedirs(ruta_absoluta)

        archivo_guardado = os.path.join(ruta_absoluta, archivo.filename)
        print(archivo_guardado)
        archivo.save(archivo_guardado)

    def convertir_a_mp4(self, nombre_archivo):
        ruta_relativa_original = os.path.join('.', 'files\original')
        ruta_absoluta_original = os.path.abspath(ruta_relativa_original)

        ruta_relativa_convertido = os.path.join('.', 'files\convertido\ideo.mp4')
        ruta_absoluta_convertido = os.path.abspath(ruta_relativa_convertido)

        ruta_archivo_convertir = os.path.join(ruta_absoluta_original, nombre_archivo)

        video = VideoFileClip(ruta_archivo_convertir)

        video.write_videofile(ruta_relativa_convertido, codec='libx264')

    def convertir_a_webm(self, nombre_archivo):

        ruta_relativa_original = os.path.join('.', 'files\original')
        ruta_absoluta_original = os.path.abspath(ruta_relativa_original)

        ruta_relativa_convertido = os.path.join('.', 'files\convertido\ideo.webm')
        ruta_absoluta_convertido = os.path.abspath(ruta_relativa_convertido)

        ruta_archivo_convertir = os.path.join(ruta_absoluta_original, nombre_archivo)

        print('ruta_archivo_convertir')
        print(ruta_archivo_convertir)

        video = VideoFileClip(ruta_archivo_convertir)

        print('ruta_absoluta_convertido')
        print(ruta_absoluta_convertido)
        video.write_videofile(ruta_absoluta_convertido, codec='libvpx')

    def convertir_a_avi(self, nombre_archivo):
        
        ruta_relativa_original = os.path.join('.', 'files\original')
        ruta_absoluta_original = os.path.abspath(ruta_relativa_original)

        ruta_relativa_convertido = os.path.join('.', 'files\convertido\ideo.avi')
        ruta_absoluta_convertido = os.path.abspath(ruta_relativa_convertido)

        ruta_archivo_convertir = os.path.join(ruta_absoluta_original, nombre_archivo)

        video = VideoFileClip(ruta_archivo_convertir)

        video.write_videofile(ruta_absoluta_convertido, codec='rawvideo')

    def crear_estado_documento(self, nombre_archivo, estado, extension_original, extension_convertir):
        estado_archivos = EstadoArchivos(
                nombre_archivo=nombre_archivo,
                extension_original=extension_original,
                extension_nueva=extension_convertir,
                estado=estado
        )   

        db.session.add(estado_archivos)
        db.session.commit()

        return estado_archivos

    def editar_estado_documento(self, id, estado):

        estado_archivo = EstadoArchivos.query.get(id)
        estado_archivo.estado = estado
        db.session.commit()

    def obtener_estado_tareas_por_id(self, id):
        return EstadoArchivos.query.get(id)

    
