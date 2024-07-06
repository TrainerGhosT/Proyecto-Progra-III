# Menu principal de la aplicación
from registros.colaboradores import registrar_colaborador
from registros.horas import registrar_horas

def menu_mostrar():
    print('Proyecto de Programación III')    
    while True:
        print("\nMenú de opciones:")
        print("1. Registrar colaborador")
        print("2. Registrar horas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            codigo = input("Ingrese el código del colaborador: ")
            nombre = input("Ingrese el nombre del colaborador: ")
            clave = input("Ingrese la clave del colaborador: ")
            posicion = input("Ingrese la posición del colaborador: ")
            registrar_colaborador(codigo, nombre, clave, posicion)
        
        elif opcion == '2':
            codigo = input("Ingrese el código del colaborador: ")
            dia = int(input("Ingrese el día de la semana (0-5, donde 0 es lunes y 5 es sábado): "))
            horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            registrar_horas(codigo, dia, horas_trabajadas)
        
        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")