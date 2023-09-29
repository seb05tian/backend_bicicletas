from config.db import app, db, ma

class Ruta(db.Model):
    __tablename__ = "tblrutas"

    id_ruta = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id_usuario'))
    latitud = db.Column(db.String(250))
    longitud = db.Column(db.String(250))
    ruta_propuesta = db.Column(db.String(250))
    fecha = db.Column(db.DateTime)
    hora= db.Column(db.DateTime)

    def __init__(self, id_ruta, id_usuario, latitud, longitud,ruta_propuesta, fecha, hora):
        self.id_ruta=id_ruta
        self.id_usuario = id_usuario 
        self.longitud=longitud
        self.latitud=latitud
        self.ruta_propuesta=ruta_propuesta
        self.fecha=fecha
        self.hora=hora

with app.app_context():
    db.create_all()

class RutaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idcliente',"latitud","longitud",'ruta_propuesta', 'fecha', 'hora')