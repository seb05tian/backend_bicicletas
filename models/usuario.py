from config.db import app, db, ma

class usuario(db.Model):
    __tablename__ = "tblusuario"

    id_usuario = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nombre_usuario = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))
    correo_electronico = db.Column(db.String(100))
   


    def __init__(self, nombre_usuario , contraseña , correo_electronico ):
        
        self.nombre_usuario = nombre_usuario
        self.contraseña=contraseña
        self.correo_electronico=correo_electronico
        

with app.app_context():
    db.create_all()

class usuarioSchema(ma.Schema):
    class Meta:
        fields = ('id_usuario' , 'nombre_usuario' , 'contraseña' , 'correo_electronico')