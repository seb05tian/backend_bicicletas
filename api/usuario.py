from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.usuario import usuario, usuarioSchema

ruta_usuario = Blueprint("ruta_usuario",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

UsuarioSchema = usuarioSchema()
UsuarioSchema= usuarioSchema(many=True)

@ruta_usuario.route("/usuario", methods=["GET"])
def usuario():
    resultall = usuario.query.all()
    result = usuarioSchema.dump(resultall)
    return jsonify(result)

@ruta_usuario.route("/saveusuario", methods=["POST"])
def saveusuario():
    nombre = request.json['nombre_usuario']
    new_usuario = usuario(nombre)
    db.session.add(new_usuario)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_usuario.route("/updateusuario", methods=["PUT"])
def updateusuario():
    id = request.json['id']
    nombre = request.json['nombre_usuario']
    nusuario = usuario.query.get(id) #Select * from Cliente where id = id
    nusuario.nombre = nombre
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_usuario.route("/deletecliente/<id>", methods=["GET"])
def deleteusuario(id):
    usuario = usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(usuarioSchema.dump(usuario))
 
 