from Data import cargar_datos, guardar_datos

trainers = cargar_datos('trainers.json')

def registrar_trainer(id, nombres, apellidos, especialidad):
    trainer = {
        "id": id,
        "nombres": nombres,
        "apellidos": apellidos,
        "especialidad": especialidad,
        "rutas_asignadas": []
    }
    trainers.append(trainer)
    guardar_datos('trainers.json', trainers)

def listar_trainers():
    return trainers
