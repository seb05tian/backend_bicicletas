from flask import Flask, redirect, jsonify, render_template, request, session
from config.bd import app, db
from sqlalchemy import text


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
    if request.method == 'POST' and 'usuario' in request.form and 'password' in request.form:
        _user = request.form['usuario']
        _pass = request.form['password']

        sql_query = text('SELECT * FROM tblusuario WHERE nombre_usuario = :user AND contraseña = :pass')
        result = db.session.execute(sql_query, {'user': _user, 'pass': _pass})
        account = result.fetchone()

        if account:
            # Accede a los elementos de la tupla por posición numérica
            id_usuario = account[0]
            nombre_usuario = account[1]
            contraseña = account[2]

            session['logueado'] = True
            session['id_usuario'] = id_usuario
            return render_template("index.html")

    return render_template("login.html")




@app.route('/index', methods=['GET'])
def inicio():
    return render_template("index.html")

@app.route('/chat', methods=['GET'])
def chat():
    
    return render_template("Chat.html")

@app.route('/mapa', methods=['GET'])
def mapa():
    
    return render_template("Mapa.html")

@app.route('/Registrar', methods=['GET'])
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
