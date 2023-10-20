from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

EstadoEnum = Enum('Ingresado','procesando', 'convertido', 'fallido', name='estado_enum')
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
