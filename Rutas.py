from Data import cargar_datos, guardar_datos
from Data import cargar_datos, guardar_datos
import json
campers = cargar_datos('campers.json')

rutas_entrenamiento = cargar_datos('rutas_entrenamiento.json')

def crear_ruta_entrenamiento(id, nombre, modulos, capacidad_maxima, area_entrenamiento, campers_asignados):
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
        if len(ruta["campers_asignados"]) < int(ruta["capacidad_maxima"]):
            ruta["campers_asignados"].append(camper["id"])
            camper["estado"] = "Cursando"
            guardar_datos('campers.json', campers)
            guardar_datos('rutas_entrenamiento.json', rutas_entrenamiento)
        else:
            raise Exception("Capacidad máxima alcanzada")
    else:
        raise Exception("Camper o Ruta no encontrados")
trainers = cargar_datos('trainers.json')

    
def asignar_trainer_a_ruta(id_trainer, id_ruta):
    trainer = next((t for t in trainers if t["id"] == id_trainer), None)
    ruta = next((r for r in rutas_entrenamiento if r["id"] == id_ruta), None)
        
    if trainer and ruta:
        if not ruta.get("trainer"):
            ruta["trainer"] = trainer["id"]
            guardar_datos('rutas_entrenamiento.json', rutas_entrenamiento)
        else:
                raise Exception("Ya hay un trainer asignado a esta ruta")
    else:
        raise Exception("Trainer o Ruta no encontrados")
    
def mostrar_informacion(ruta):
    try:
        with open(ruta) as contenido:
            datos_usuario = json.load(contenido)
            for usuario, datos in datos_usuario["ingresados"].items():
                print (f"información del usuario {usuario}:")
                print (f"Nombres: {datos["nombres"]}")
                print (f"Apellidos: {datos["apellidos"]}")
                print (f"Dirección: {datos["direccion"]}")     
    except Exception:   
        print("Error")     
