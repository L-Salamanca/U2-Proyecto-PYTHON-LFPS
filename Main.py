#Trabajo Realizado por: 
#Luis Fernando Pérez Salamanca
#U2


from Campers import *
from Trainers import *
from Rutas import *
from reportes import *
from Data import *

    
def main():


        
    print("Bienvenido a CampusLands")
    while True:
        try:
            print("  ____                                _                 _     ")
            print(" / ___|__ _ _ __ ___  _ __  _   _ ___| | __ _ _ __   __| |___ ")
            print("| |   / _` | '_ ` _ \| '_ \| | | / __| |/ _` | '_ \ / _` / __|")
            print("| |__| (_| | | | | | | |_) | |_| \__ \ | (_| | | | | (_| \__ \\")
            print(" \____\__,_|_| |_| |_| .__/ \__,_|___/_|\__,_|_| |_|\__,_|___/")
            print("                     |_|                                      \n")
            print("                     ingrese una opcion:\n")
            print("                  1. Opciones de Camper")
            print("                  2. Opciones de Trainer")
            print("                  3. Ingresar como coordinador")
            print("                  4. Salir\n")

            opcion = input("Seleccione una opción: ")
        
        
        
            if opcion == "1":
                print("\n")
                print("                 ingrese una opcion:\n")
                print("              1. Registrar Camper")
                print("              2. Ver notas de Camper")
                print("              3. Comprobar rutas disponibles")
                print("              4. Retirarse de Campuslands")
                print("              5. Salir")
                sub_opcion3 = input ("Seleccione una opcion:\n ")
                if sub_opcion3 == "1":
                    id = input("ID: ")
                    nombres = input("Nombres: ")
                    apellidos = input("Apellidos: ")
                    direccion = input("Dirección: ")    
                    acudiente = input("Acudiente: ")
                    telefono_celular = input("Teléfono Celular: ")
                    telefono_fijo = input("Teléfono Fijo: ")
                    estado = "Inscrito"
                    riesgo = None
                    registrar_camper(id, nombres, apellidos, direccion, acudiente, telefono_celular, telefono_fijo, estado, riesgo)
                    print("Usuario inscrito con exito")
                    
                elif sub_opcion3 == "2":
                    id_camper = input("ID del Camper: ")
                    print(nota_teorica)
                    print(nota_practica)
                    print(nota_quiz_trabajos)
                    nota_final = obtener_nota_final(id_camper)
                    print("La nota final del camper es: ", nota_final)
                    
                elif sub_opcion3 =="3":
                    print (rutas_entrenamiento)
                    
                elif sub_opcion3=="4":
                    id_camper = input("ID del Camper: ")
                    eliminar_camper(id_camper)
                    print ("Cuenta eliminada con exito")
                    
                    
            elif opcion == "2":
                print("\n")
                print("                 ingrese una opcion:\n")
                print("              1. Registrar Trainer")
                print("              2. Ver nota de Camper")
                print("              3. Asignar nota de camper")
                print("              4. Salir")
                sub_opcion4 = input ("Seleccione una opcion:\n ")
                if sub_opcion4 == "1":  
                    id = input("ID: ")
                    nombres = input("Nombres: ")
                    apellidos = input("Apellidos: ")
                    especialidad = input("Especialidad: ")
                    horario = input("horario:(6:00am-10:00am/2:00pm-6:00pm: )")
                    registrar_trainer(id, nombres, apellidos, especialidad,horario)
                    
                elif sub_opcion4 =="2":
                    id_camper = input("ID del Camper: ")
                    print(nota_teorica)
                    print(nota_practica)
                    print(nota_quiz_trabajos)
                    nota_final = obtener_nota_final(id_camper)
                    print("La nota final del camper es: ", nota_final)
                                        
                elif sub_opcion4 == "3":
                        id_camper = input("ID del Camper: ")
                        nota_teorica = float(input("Nota teórica del Camper: "))
                        nota_practica = float(input("Nota práctica del Camper: "))
                        nota_quiz_trabajos = float(input("Nota de quiz y trabajos del Camper: "))
                        evaluar_camper(id_camper, nota_teorica, nota_practica, nota_quiz_trabajos)
            
            elif opcion == "3":
                contraseña=input("Ingrese la contraseña de coordinador: ")
                if contraseña == "coordinador1234":
                    print("                Bienvenido Coordinador")
                    print("               1. Asignar Camper a ruta")
                    print("               2. Evaluar Camper")
                    print("               3. Eliminar Campers")
                    print("               4. Crear Ruta de Entrenamiento")
                    print("               5. Asignar Trainer a Ruta")
                    print("               6. Reportes")
                    sub_opcion = input("Seleccione una opción: ")
                    if sub_opcion == "1":
                        id_camper = input("ID del Camper: ")
                        id_ruta = input("ID de la Ruta: ")
                        asignar_camper_a_ruta(id_camper, id_ruta)
                    elif sub_opcion == "2":
                        id_camper = input("ID del Camper: ")
                        nota_teorica = float(input("Nota teórica del Camper: "))
                        nota_practica = float(input("Nota práctica del Camper: "))
                        nota_quiz_trabajos = float(input("Nota de quiz y trabajos del Camper: "))
                        evaluar_camper(id_camper, nota_teorica, nota_practica, nota_quiz_trabajos)
                    elif sub_opcion == "3":
                        id_camper = input("ID del Camper: ")
                        eliminar_camper(id_camper)
                    elif sub_opcion == "4":
                        id = input("ID de la Ruta: ")
                        nombre = input("Nombre de la Ruta: ")
                        modulos = input("Módulos de la Ruta: ")
                        capacidad_maxima = input("Capacidad Máxima de la Ruta: ")
                        area_entrenamiento = input("Área de Entrenamiento de la Ruta: ")
                        campers_asignados = []
                        crear_ruta_entrenamiento(id, nombre, modulos, capacidad_maxima, area_entrenamiento, campers_asignados)
                    elif sub_opcion == "5":
                        id_trainer = input("ID del Trainer: ")
                        id_ruta = input("ID de la Ruta: ")
                        asignar_trainer_a_ruta(id_trainer, id_ruta)
                    elif sub_opcion == "6":
                        print("1. Listar Campers Inscritos")
                        print("2. Listar Campers Aprobados")
                        print("3. Listar Trainers")
                        print("4. Listar Campers con Bajo Rendimiento")
                        print("5. Listar Asignaciones")
                        print("6. Mostrar Resultados de Módulos")
                        sub_opcion2 = input("Seleccione una opción: ")
                        if sub_opcion2 == "1":
                            campers_inscritos = listar_campers_inscritos()
                            for camper in campers_inscritos:
                                print(camper)
                        elif sub_opcion2 == "2":
                            campers_aprobados = listar_campers_aprobados()
                            for camper in campers_aprobados:
                                print(camper)
                        elif sub_opcion2 == "3":
                            trainers = listar_trainers()
                            for trainer in trainers:
                                print(trainer)
                        elif sub_opcion2 == "4":
                            bajo_rendimiento = listar_campers_bajo_rendimiento()
                            for camper in bajo_rendimiento:
                                print(camper)
                        elif sub_opcion2 == "5":
                            asignaciones = listar_asignaciones()
                            for asignacion in asignaciones:
                                print(asignacion)
                        elif sub_opcion2 == "6":
                            resultados = mostrar_resultados_modulos()
                            for resultado in resultados:
                                print(resultado)
            elif opcion == "4":
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
        except Exception as e:
            print("Error: ", e)
        except:
            print("Error inesperado")
        finally:
            print("Gracias por usar CampusLands")

    
if __name__ == "__main__":
    main()

