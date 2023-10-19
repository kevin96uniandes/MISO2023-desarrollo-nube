from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app import db
from sqlalchemy import Enum

EstadoEnum = Enum('Ingresado','procesando', 'convertido', 'fallido')

class EstadoArchivos(db.Model):

    __tablename__ = 'estado_archivos'
    id = db.Column(db.Integer, primary_key=True)
    nombre_archivo = db.Column(db.String(128))
    extension_original = db.Column(db.String(128))
    extension_nueva = db.Column(db.String(128))
    estado = db.Column(EstadoEnum, nullable=False)

class EstadoArchivosSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EstadoArchivos
        include_relationships = True
        load_instance = True
        include_fk = True

    id = fields.String()
