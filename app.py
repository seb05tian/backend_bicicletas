from flask import Flask, redirect, jsonify, render_template, request, json, session
from config.bd import app, db

from api.usuario import ruta_usuario
from api.Ruta import  ruta_ruta
from api.comunidad import  ruta_comunidad
from api.alerta import  ruta_alerta

app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_ruta, url_prefix="/api")
app.register_blueprint(ruta_comunidad, url_prefix="/api")
app.register_blueprint(ruta_alerta, url_prefix="/api")



@app.route('/', methods=['GET'])
def index():
    return render_template("login.html")
    

@app.route("/savegps",methods=["POST"])
def savegps():
    latitud  = request.json['latitud']
    longitud = request.json[ 'longitud']
    print(latitud)
    return jsonify(longitud)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')