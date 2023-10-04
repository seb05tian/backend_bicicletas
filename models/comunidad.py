from config.db import app, db, ma

class comunidad(db.Model):
    __tablename__ = "tblcomunidad"

    id_comunidad = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id_usuario'))
    Nombre_comunidad = db.Column(db.String(100))
    comentario = db.Column(db.String(100))
    fecha = db.Column(db.Date)



    def __init__(self , id_comunidad, id_usuario , Nombre_comunidad , comentario, fecha):
        self.id_comunidad=id_comunidad
        self.id_usuario=id_usuario
        self.Nombre_comunidad=Nombre_comunidad
        self.comentario=comentario
        self.fecha=fecha
        
    

with app.app_context():
    db.create_all()

class comunidadSchema(ma.Schema):
    class Meta:
        fields = ('id_comunidad', 'id_usuario' , 'Nombre_comunidad' , 'comentario', 'fecha')