from Data import *
import json
trainers = cargar_datos('trainers.json')

def registrar_trainer(id, nombres, apellidos, especialidad,horario):
    trainer = {
        "id": id,
        "nombres": nombres,
        "apellidos": apellidos,
        "especialidad": especialidad,
        "horario": horario,
        "rutas_asignadas": []
    }
    trainers.append(trainer)
    guardar_datos('trainers.json', trainers)

def listar_trainers():
    return trainers

def buscar_trainer_por_id(id_trainer):
    
    trainer = next((t for t in trainers if t["id"] == id_trainer), None)

    if trainer is None:
        print(f"No se encontró un trainer con el ID {id_trainer}")
        return None

    return trainer
