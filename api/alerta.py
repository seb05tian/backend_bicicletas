from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.alerta import alerta, alertaSchema

ruta_alerta = Blueprint("ruta_alerta",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

community_schema = alertaSchema()
community_schema = alertaSchema(many=True)

@ruta_alerta.route("/alerta", methods=["GET"])
def alerta():
    resultall = alerta.query.all()# Select * from Ruta;
    result = alertaSchema.dump(resultall)
    return jsonify(result)


@ruta_alerta.route("/savealerta", methods=["POST"])
def savecomunidad():
    data = request.get_json()
    db.session.add(alerta(**data))
    db.session.commit()
    return community_schema.jsonify(alerta(**data))





@ruta_alerta.route("/deletealerta/<id>", methods=["GET"])
def deletealerta(id_alerta):
   comunidad = alerta.query.get(id_alerta)
   db.session.delete(comunidad)
   db.session.commit()
    
   return jsonify(alertaSchema.dump(alerta))


