from registros.colaboradores import registrar_colaborador, obtener_colaboradores
from registros.horas import registrar_horas
from planilla.calculo import calcular_salarios
from planilla.reporte import generar_reporte
from archivos.generar_archivo import escribir_empleados, escribir_horas, leer_empleados, leer_horas, verificar_carpeta_data

planilla_generada = False

def menu():
    verificar_carpeta_data()  # Aseguramos que la carpeta data existe al iniciar el programa

    global planilla_generada

    while True:
        print("Menú Principal")
        print("1. Registro de nombres para los colaboradores")
        print("2. Registro de horas para cada colaborador")
        print("3. Generar planilla")
        print("4. Reporte de planilla")
        print("5. Escribir en archivo")
        print("6. Reporte desde archivo")
        print("7. Limpiar los datos")
        print("8. Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            codigo = input("Ingrese el código del colaborador: ")
            nombre = input("Ingrese el nombre del colaborador: ")
            clave = input("Ingrese la clave del colaborador: ")
            try:
                posicion = int(input("Ingrese la posición del colaborador en la matriz: "))
                registrar_colaborador(codigo, nombre, clave, posicion)
            except ValueError:
                print ("La posicion debe ser un numero entero")

        elif opcion == '2':
            codigo = input("Ingrese el código del colaborador: ")
            try:
                dia = int(input("Ingrese el día de la semana (0(lunes) - 5(sábado)): "))
                if dia < 0 or dia > 5:
                    raise ValueError ("Dia incorrecto, ingrese un valor entre 0 y 5")
                horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
                registrar_horas(codigo, dia, horas_trabajadas)
            except ValueError as ex:
                print(f"Error: {ex}")

        elif opcion == '3':
            calcular_salarios()
            planilla_generada = True
            print("Planilla generada con éxito.")

        elif opcion == '4':
            if not planilla_generada:
                print("Debe generar la planilla antes de poder ver el reporte.")
            else:
                generar_reporte()

        elif opcion == '5':
            if not planilla_generada:
                print("Debe generar la planilla y ver el reporte antes de escribir en archivo.")
            else:
                escribir_empleados()
                escribir_horas()
                print("Datos escritos en archivo con éxito.")

        elif opcion == '6':
            colaboradores = leer_empleados()
            leer_horas(colaboradores)
            for codigo, datos in colaboradores.items():
                print(f"Colaborador: {datos['nombre']}")
                print(f"Horas ordinarias: {sum(min(h, 4) for h in datos['horas'])}")
                print(f"Horas extraordinarias: {sum(max(0, h - 4) for h in datos['horas'])}")

        elif opcion == '7':
            obtener_colaboradores().clear()
            planilla_generada = False
            print("Datos limpiados con éxito.")

        elif opcion == '8':
            break

        else:
            print("Opción no valida")


