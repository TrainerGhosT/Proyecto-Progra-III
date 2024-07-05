# main.py
from registros.colaboradores import registrar_colaborador
from registros.horas import registrar_horas

def main():
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
            dia = int(input("Ingrese el día de la semana (0-6, donde 0 es lunes y 6 es domingo): "))
            horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            registrar_horas(codigo, dia, horas_trabajadas)
        
        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
