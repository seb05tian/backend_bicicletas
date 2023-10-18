from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.alerta import alerta, alertaSchema

ruta_alerta = Blueprint("ruta_alerta",__name__)



alertas_schema = alertaSchema(many=True)
alerta_schema = alertaSchema()

@ruta_alerta.route("/alerta", methods=["GET"])
def alerta():
    resultall = alerta.query.all()
    result = alertas_schema.dump(resultall)
    return jsonify(result)


@ruta_alerta.route("/savealerta", methods=["POST"])
def save_alerta():
    data = request.get_json()
    db.session.add(alerta(**data))
    db.session.commit()
    return jsonify(alerta_schema.dump(alerta(**data)))


@ruta_alerta.route("/updatealerta", methods=["PUT"])
def updatealerta():
    id_alerta = request.json['id_alerta']
    id_ruta=request.json['id_ruta']
    tipo_alerta=request.json['tipo_alerta']
    descripcion=request.json['descripcion']
    fecha=request.json['fecha']
    hora=request.json['hora']
    nalerta = alerta.query.get(id_alerta) 
    nalerta.id_ruta=id_ruta
    nalerta.tipo_alerta=tipo_alerta
    nalerta.descripcion=descripcion
    nalerta.fecha=fecha
    nalerta.hora=hora
    db.session.commit()
    return "Datos Actualizado con exitos"


@ruta_alerta.route("/deletealerta/<id>", methods=["GET"])
def deletealerta(id_alerta):
   data = alerta.query.get(id_alerta)
   db.session.delete(data)
   db.session.commit()
    
   return jsonify(alertaSchema.dump(data))


