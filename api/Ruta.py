from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
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
    ubicacion_partida = ubicacion_partida.json['ubicacion_partida']
    ubicacion_destino = ubicacion_destino.json['ubicacion_destino']
    ruta_propuesta=ruta_propuesta.json['ruta_propuesta']
    
   

    nruta = Ruta.query.get(id_ruta) 
    nruta.id_usuario=id_usuario
    nruta.ubicacion_partida=ubicacion_partida
    nruta.ubicacion_destino=ubicacion_destino
    nruta.ruta_propuesta=ruta_propuesta

    db.session.commit()
    return "Datos Actualizado con exitos."





@ruta_ruta.route("/deleteruta/<id>", methods=["GET"])
def deleteruta(id):
    data = Ruta.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify(ruta_schema.dump(data))






