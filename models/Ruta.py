from config.bd import app, db, ma

class Ruta(db.Model):
    __tablename__ = "tblrutas"

    id_ruta = db.Column(db.Integer, primary_key = True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id_usuario'))
    ubicacion_partida = db.Column(db.String(250))
    ubicacion_destino = db.Column(db.String(250))
    ruta_propuesta = db.Column(db.String(250))
    

    

    def __init__(self, id_usuario, ubicacion_partida, ubicacion_destino,ruta_propuesta):
        self.id_usuario = id_usuario 
        self.ubicacion_partida=ubicacion_partida
        self.ubicacion_destino=ubicacion_destino
        self.ruta_propuesta=ruta_propuesta
        
        

with app.app_context():
    db.create_all()

class RutaSchema(ma.Schema):
    class Meta:
        fields = ('id_ruta', 'id_usuario',"ubicacion_partida","ubicacion_destino",'ruta_propuesta')