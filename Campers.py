from Data import cargar_datos, guardar_datos

campers = cargar_datos('campers.json')

def registrar_camper(id, nombres, apellidos, direccion, acudiente, telefono_celular, telefono_fijo, estado, riesgo):
    camper = {
        "id": id,
        "nombres": nombres,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefono_celular": telefono_celular,
        "telefono_fijo": telefono_fijo,
        "estado": estado,
        "riesgo": riesgo,
        "notas": []
    }
    campers.append(camper)
    guardar_datos('campers.json', campers)

def evaluar_camper(id_camper, modulo, nota_teorica, nota_practica, nota_quiz_trabajos):
    camper = next((c for c in campers if c["id"] == id_camper), None)
    if camper:
        nota_final = (0.3 * nota_teorica) + (0.6 * nota_practica) + (0.1 * nota_quiz_trabajos)
        camper["notas"].append({
            "modulo": modulo,
            "nota_teorica": nota_teorica,
            "nota_practica": nota_practica,
            "nota_quiz_trabajos": nota_quiz_trabajos,
            "nota_final": nota_final
        })
        if nota_final >= 60:
            camper["estado"] = "Aprobado"
        guardar_datos('campers.json', campers)
        return nota_final
    else:
        raise Exception("Camper no encontrado")

def listar_campers_inscritos():
    return [c for c in campers if c["estado"] == "Inscrito"]

def listar_campers_aprobados():
    return [c for c in campers if c["estado"] == "Aprobado"]

def listar_campers_bajo_rendimiento():
    return [c for c in campers if any(nota["nota_final"] < 60 for nota in c["notas"])]
