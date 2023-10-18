import pytz 
from config.bd import app, db, ma
from datetime import datetime
class comunidad(db.Model):
    __tablename__ = "tblcomunidad"

    id_comunidad = db.Column(db.Integer, primary_key = True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id_usuario'))
    nombre_usuario= db.Column(db.String(50))
    Nombre_comunidad = db.Column(db.String(100), default='ciclistasvip')
    comentario = db.Column(db.String(100))
    fecha = db.Column(db.DateTime)



    def __init__(self, id_usuario,nombre_usuario, comentario):
        self.id_usuario=id_usuario
        self.comentario=comentario
        self.nombre_usuario=nombre_usuario
        self.fecha = datetime.now(pytz.timezone('America/Bogota'))
        
    

with app.app_context():
    db.create_all()

class comunidadSchema(ma.Schema):
    class Meta:
        fields = ('id_comunidad', 'id_usuario' , 'nombre_usuario', 'Nombre_comunidad' , 'comentario', 'fecha')