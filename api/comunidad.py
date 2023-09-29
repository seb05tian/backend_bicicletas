from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.comunidad import comunidad, comunidadSchema

ruta_comunidad = Blueprint("ruta_comunidad",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

community_schema = comunidadSchema()
community_schema = comunidadSchema(many=True)

@ruta_comunidad.route("/comunidad", methods=["GET"])
def communidad():
    resultall = comunidad.query.all()# Select * from Ruta;
    result = comunidadSchema.dump(resultall)
    return jsonify(result)


@ruta_comunidad.route("/saveCommunidad", methods=["POST"])
def savecomunidad():
    data = request.get_json()
    db.session.add(comunidad(**data))
    db.session.commit()
    return community_schema.jsonify(comunidad(**data))





@ruta_comunidad.route("/deletecomunidad/<id>", methods=["GET"])
def deletecomunidad(id):
   comunidad = comunidad.query.get(id)
   db.session.delete(comunidad)
   db.session.commit()
    
   return jsonify(comunidadSchema.dump(comunidad))




