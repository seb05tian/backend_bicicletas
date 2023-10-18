from flask import Flask, redirect, jsonify, render_template, request, session
from config.bd import app, db
from sqlalchemy import text
from models.usuario import usuario
from models.comunidad import comunidad, comunidadSchema
from api.usuario import ruta_usuario
from api.Ruta import ruta_ruta
from api.comunidad import ruta_comunidad
from api.alerta import ruta_alerta

app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_ruta, url_prefix="/api")
app.register_blueprint(ruta_comunidad, url_prefix="/api")
app.register_blueprint(ruta_alerta, url_prefix="/api")



@app.route('/', methods=['GET', 'POST'])
def login():
    

    return render_template("login.html")




@app.route('/index', methods=['GET'])
def inicio():
    return render_template("index.html")

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        # Si la solicitud es un POST, significa que se está enviando un nuevo comentario
        nombre_usuario = request.form.get("nombre_usuario")
        comentario = request.form.get("comentario")

        usuario_existente = usuario.query.filter_by(nombre_usuario=nombre_usuario).first()
        if not usuario_existente:
            return render_template("Chat.html")

        nuevo_comentario = comunidad(id_usuario=usuario_existente.id_usuario, nombre_usuario=nombre_usuario, comentario=comentario, )
        db.session.add(nuevo_comentario)
        db.session.commit()

    # Obtén todos los comentarios de la base de datos
    comentarios = comunidad.query.all()

    return render_template('Chat.html', comentarios=comentarios)


@app.route('/mapa', methods=['GET'])
def mapa():
    
    return render_template("Mapa.html")

@app.route('/Registrar', methods=['GET', 'POST'])
def register():
   
    
    return render_template("register.html")


@app.route("/savegps",methods=["POST"])
def savegps():
    latitud  = request.json['latitud']
    longitud = request.json[ 'longitud']
    print(latitud)
    return jsonify(longitud)




if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
