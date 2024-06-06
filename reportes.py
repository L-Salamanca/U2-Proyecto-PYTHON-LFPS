from Data import *
from Rutas import *
from Trainers import *
import json

def listar_asignaciones():
    asignaciones = []
    for ruta in rutas_entrenamiento:
        trainer = buscar_trainer_por_id(ruta["trainer"])
        if trainer is not None:
            asignacion = {
                "ruta": ruta["nombre"],
                "campers": [c for c in campers if c["id"] in ruta["campers_asignados"]],
                "trainer": trainer["nombres"] + " " + trainer["apellidos"]
            }
            asignaciones.append(asignacion)
    return asignaciones

def mostrar_resultados_modulos():
    resultados = []
    for ruta in rutas_entrenamiento:
        resultado_modulo = {
            "ruta": ruta["nombre"],
            "resultados": []
        }
        for camper_id in ruta["campers_asignados"]:
            camper = next((c for c in campers if c["id"] == camper_id), None)
            if camper:
                for nota in camper["notas"]:
                    resultado_modulo["resultados"].append({
                        "camper": camper["nombres"] + " " + camper["apellidos"],
                        "modulo": nota["modulo"],
                        "nota_final": nota["nota_final"]
                    })
        resultados.append(resultado_modulo)
    return resultados
