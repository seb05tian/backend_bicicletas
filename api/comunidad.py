from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.comunidad import comunidad, comunidadSchema

ruta_comunidad = Blueprint("ruta_comunidad",__name__)



communitys_schema = comunidadSchema(many=True)
community_schema = comunidadSchema()





@ruta_comunidad.route("/comunidad", methods=["GET"])
def communidad():
    resultall = comunidad.query.all()
    result = communitys_schema.dump(resultall)
    return jsonify(result)


@ruta_comunidad.route("/savecomunidad", methods=["POST"])
def savecomunidad():
    data = request.get_json()
    db.session.add(comunidad(**data))
    db.session.commit()
    return jsonify(community_schema.dump(comunidad(**data)))


@ruta_comunidad.route("/updatecomunidad", methods=["PUT"])
def updatecomunidad():
    id_comunidad = request.json['id_comunidad']
    id_usuario=request.json['id_usuario']
    nombre=request.json['nombre']
    nombre_comunidad=request.json['Nombre_comunidad']
    comentario=request.json['comentario']
   
    ncomunidad = comunidad.query.get(id_comunidad) 
    ncomunidad.id_usuario=id_usuario
    ncomunidad.nombre_comunidad=nombre_comunidad
    ncomunidad.comentario=comentario
    ncomunidad.nombre=nombre
    db.session.commit()
    return "Datos Actualizado con exitos"


@ruta_comunidad.route("/deletecomunidad/<id>", methods=["GET"])
def deletecomunidad(id):
   data = comunidad.query.get(id)
   db.session.delete(data)
   db.session.commit()
    
   return jsonify(community_schema.dump(data))




