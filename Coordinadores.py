from Data import cargar_datos, guardar_datos

coordinadores = cargar_datos('coordinadores.json')

def registrar_coordinador(id, nombres, apellidos):
    coordinador = {
        "id": id,
        "nombres": nombres,
        "apellidos": apellidos
    }
    coordinadores.append(coordinador)
    guardar_datos('coordinadores.json', coordinadores)
