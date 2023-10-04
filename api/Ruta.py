from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Ruta import Ruta, RutaSchema

ruta_ruta = Blueprint("ruta_ruta",__name__)


rutas_schema = RutaSchema(many=True)
ruta_schema = RutaSchema()
@ruta_ruta.route("/rutas", methods=["GET"])
def ruta():
    resultall = Ruta.query.all()
    result = rutas_schema.dump(resultall)
    return jsonify(result)



@ruta_ruta.route("/saveruta", methods=["POST"])
def saveruta():
    data = request.get_json()
    db.session.add(Ruta(**data))
    db.session.commit()
    return jsonify(ruta_schema.dump(Ruta(**data)))



@ruta_ruta.route("/updateruta", methods=["PUT"])
def updateruta():
    id_ruta = request.json['id_ruta']
    id_usuario=request.json['id_usuario']
    latitud = latitud.json['latitud']
    longitud = longitud.json['longitud']
    ruta_propuesta=ruta_propuesta.json['ruta_propuesta']
    fecha=fecha.json['fecha']
   

    nruta = Ruta.query.get(id_ruta) #Select * from ruta where id = id
    nruta.id_usuario=id_usuario
    nruta.longitud=longitud
    nruta.latitud=latitud
    nruta.ruta_propuesta=ruta_propuesta
    nruta.fecha=fecha

    db.session.commit()
    return "Datos Actualizado con exitos."





@ruta_ruta.route("/deleteruta/<id>", methods=["GET"])
def deleteruta(id):
    data = Ruta.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify(ruta_schema.dump(data))






