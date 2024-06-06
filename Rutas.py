from Data import cargar_datos, guardar_datos

campers = cargar_datos('campers.json')

rutas_entrenamiento = cargar_datos('rutas_entrenamiento.json')

def crear_ruta_entrenamiento(id, nombre, modulos, capacidad_maxima, area_entrenamiento):
    ruta = {
        "id": id,
        "nombre": nombre,
        "modulos": modulos,
        "capacidad_maxima": capacidad_maxima,
        "area_entrenamiento": area_entrenamiento,
        "campers_asignados": []
    }
    rutas_entrenamiento.append(ruta)
    guardar_datos('rutas_entrenamiento.json', rutas_entrenamiento)

def asignar_camper_a_ruta(id_camper, id_ruta):
    camper = next((c for c in campers if c["id"] == id_camper), None)
    ruta = next((r for r in rutas_entrenamiento if r["id"] == id_ruta), None)
    
    if camper and ruta:
        if len(ruta["campers_asignados"]) < ruta["capacidad_maxima"]:
            ruta["campers_asignados"].append(camper["id"])
            camper["estado"] = "Cursando"
            guardar_datos('campers.json', campers)
            guardar_datos('rutas_entrenamiento.json', rutas_entrenamiento)
        else:
            raise Exception("Capacidad máxima alcanzada")
    else:
        raise Exception("Camper o Ruta no encontrados")
