#coding=utf-8
import msvcrt
import sys

import unirest
import json

def listarEstudiantes():
    response = unirest.get("http://localhost:4567/rest/estudiantes/", headers={"Accept": "application/json"})
    estudiantes = response.body
    for estudiante in estudiantes:
        print(estudiante)

def consultar_estudiante(matricula):
    response = unirest.get("http://localhost:4567/rest/estudiantes/" + str(matricula),headers={"Accept": "application/json"})
    estudiante = response.body
    print(estudiante)

def insertarEstudiante(nombre,correo,carrera):
    response = unirest.post('http://localhost:4567/rest/estudiantes/',
                         headers={"Content-Type": "application/json", "Accept": "application/json"},
                         params=json.dumps({"nombre": nombre, "correo": correo, "carrera": carrera}))
    print(response.body)

def menu():
    print("\nREST Client API")
    print("Seleccione una opcion:")
    print("1. Listar todos los estudiantes")
    print("2. Consultar un estudiante")
    print("3. Crear un nuevo estudiante")
    print("4.Salir")

    print("Seleccione una opción:")
    option = input()
    opciones(option)


def opciones(option):
    if option == 1:
        listarEstudiantes()
        menu()
    elif option == 2:
        matricula = raw_input("Inserte una matricula a buscar")
        consultar_estudiante(matricula)
        menu()
    elif option ==3:
        print("Digite el nombre del estudiante")
        nombre = raw_input()
        print("Digite el correo del estudiante")
        correo = raw_input()
        print("Digite la carrera del estudiante")
        carrera = raw_input()
        insertarEstudiante(nombre,correo,carrera)
        menu()
    elif option == 4:
        sys.exit("Gracias.")
    else:
        print("Seleccione una opción válida")
        menu()

menu()





