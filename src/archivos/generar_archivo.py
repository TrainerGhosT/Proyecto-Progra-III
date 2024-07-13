# Logica donde encuentra la creación y el manejo de errores de los archivos
import os
from registros.colaboradores import obtener_colaboradores


#Función para verificar si la carpeta 'data' existe
def verificar_carpeta_data():
    if not os.path.exists('data'):
        print("La carpeta data no existe. Se crea.")
        os.makedirs('data')
  
#Función para verificar si un archivo existe
def verificar_archivo(archivo):
    if not os.path.exists(archivo):
        with open(archivo, 'w') as file:
            pass

#Función para escribir la información de los empleados en 'data/empleados.txt'.
def escribir_empleados():
    verificar_carpeta_data()
    verificar_archivo('data/empleados.txt')
    colaboradores = obtener_colaboradores()
    with open('data/empleados.txt', 'w') as file:
        for codigo, datos in colaboradores.items():
            file.write(f"{codigo},{datos['nombre']},{datos['clave']},{datos['posicion']}\n")

#Función para escribir las horas laboradas por los empleados en 'data/horas_laboradas.txt'
def escribir_horas():
    verificar_carpeta_data()
    verificar_archivo('data/horas_laboradas.txt')
    colaboradores = obtener_colaboradores()
    with open('data/horas_laboradas.txt', 'w') as file:
        for codigo, datos in colaboradores.items():
            horas_str = ','.join(map(str, datos['horas']))
            file.write(f"{codigo},{horas_str}\n")

#Función para leer la información de los empleados desde 'data/empleados.txt'
def leer_empleados():
    verificar_carpeta_data()
    verificar_archivo('data/empleados.txt')
    colaboradores = {}
    with open('data/empleados.txt', 'r') as file:
        for line in file:
            codigo, nombre, clave, posicion = line.strip().split(',')
            colaboradores[codigo] = {
                'nombre': nombre,
                'clave': clave,
                'posicion': int(posicion),
                'horas': [0] * 6
            }
    return colaboradores

#Función para leer las horas laboradas por los empleados desde 'data/horas_laboradas.txt'
def leer_horas(colaboradores):
    verificar_carpeta_data()
    verificar_archivo('data/horas_laboradas.txt')
    with open('data/horas_laboradas.txt', 'r') as file:
        for line in file:
            partes = line.strip().split(',')
            codigo = partes[0]
            horas = list(map(float, partes[1:])) #cambie el int a float porque aveces pueden haber horas decimales
            if codigo in colaboradores:
                colaboradores[codigo]['horas'] = horas

