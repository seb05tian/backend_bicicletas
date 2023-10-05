from config.db import app, db, ma

class alerta(db.Model):
    __tablename__ = "tblalerta"

    id_alerta = db.Column(db.Integer, primary_key = True, autoincrement=True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('tblrutas'))
    tipo_alerta= db.Column(db.String(250))
    descripcion= db.Column(db.String(250))
    fecha = db.Column(db.Date)
    hora= db.Column(db.Time)

    def __init__(self, id_ruta, tipo_alerta, descripcion, fecha, hora):
        self.id_ruta=id_ruta
        self.tipo_alerta=tipo_alerta
        self.descripcion=descripcion
        self.fecha=fecha
        self.hora=hora
        

with app.app_context():
    db.create_all()

class alertaSchema(ma.Schema):
    class Meta:
        fields = ('id_alerta', 'id_ruta', 'tipo_alerta', 'descripcion', 'fecha', 'hora')