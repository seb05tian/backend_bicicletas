from config.bd import app, db, ma
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class usuario(db.Model):
    __tablename__ = "tblusuario"

    id_usuario = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nombre_usuario = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))
    
   


    def __init__(self, nombre_usuario , contraseña ):
        
        self.nombre_usuario = nombre_usuario
        self.contraseña=contraseña
        
        

with app.app_context():
    db.create_all()

class usuarioSchema(ma.Schema):
    class Meta:
        fields = ('id_usuario' , 'nombre_usuario' , 'contraseña')