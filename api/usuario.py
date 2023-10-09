from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.usuario import usuario, usuarioSchema

ruta_usuario = Blueprint("ruta_usuario",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)


usuarios_schema = usuarioSchema(many=True)   
usuario_schema = usuarioSchema() 
@ruta_usuario.route("/get_usuario", methods=["GET"])
def obtener_usuarios():
    resultall = usuario.query.all()
    result = usuarios_schema.dump(resultall)
    return jsonify(result)

@ruta_usuario.route("/saveusuario", methods=["POST"])
def saveusuarios():
    data= request.get_json()
    db.session.add(usuario(**data))
    db.session.commit()
    return jsonify(usuario_schema.dump(usuario(**data)))

@ruta_usuario.route("/updateusuario", methods=["PUT"])
def updateusuario():
    id_usuario = request.json['id_usuario']
    nombre = request.json['nombre_usuario']
    contraseña=request.json['contraseña']
    nusuario = usuario.query.get(id_usuario) #Select * from Cliente where id = id
    nusuario.nombre = nombre
    nusuario.contraseña=contraseña
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_usuario.route("/deletecliente/<id_usuario>", methods=["GET"])
def deleteusuario(id_usuario):
    data = usuario.query.get(id_usuario)
    db.session.delete(data)
    db.session.commit()
    return jsonify(usuario_schema.dump(data))
 
 