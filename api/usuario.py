from flask import Blueprint, jsonify, request,json, render_template
from config.bd import db, app, ma
from models.usuario import usuario, usuarioSchema
from werkzeug.security import check_password_hash

ruta_usuario = Blueprint("ruta_usuario",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)


usuarios_schema = usuarioSchema(many=True)   
usuario_schema = usuarioSchema() 




@ruta_usuario.route("/iniciar_sesion", methods=["POST"])
def iniciar_sesion():
    data = request.get_json()
    nombre_usuario = data.get("nombre_usuario")
    contraseña = data.get("contraseña")

    # Buscar al usuario por nombre de usuario
    nusuario = usuario.query.filter_by(nombre_usuario=nombre_usuario).first()

    if nusuario and nusuario.contraseña==contraseña:
        # Usuario encontrado y la contraseña es correcta
        return jsonify({"valid": True, "message": "Inicio de sesión exitoso"})
    else:
        # Usuario no encontrado o contraseña incorrecta
        return jsonify({"valid": False, "message": "Credenciales inválidas"})






@ruta_usuario.route("/saveusuario", methods=["POST"])
def saveusuarios():
    data = request.get_json()
    nombre_usuario = data.get("nombre_usuario")

    # Verifica si ya existe un usuario con el mismo nombre de usuario
    usuario_existente = usuario.query.filter_by(nombre_usuario=nombre_usuario).first()

    if usuario_existente:
        return  "El nombre de usuario ya está en uso"

    # Si no hay un usuario con el mismo nombre de usuario, registra al nuevo usuario
    nuevo_usuario = usuario(**data)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return  "Usuario registrado con éxito"


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
 
 