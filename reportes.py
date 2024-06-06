from Data import campers
from Rutas import rutas_entrenamiento

def listar_asignaciones():
    asignaciones = []
    for ruta in rutas_entrenamiento:
        campers_ruta = [c for c in campers if c["id"] in ruta["campers_asignados"]]
        asignaciones.append({
            "ruta": ruta["nombre"],
            "campers": campers_ruta
        })
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
