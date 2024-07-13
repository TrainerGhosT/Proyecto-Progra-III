from planilla.calculo import calcular_salarios
from registros.colaboradores import obtener_colaboradores

def generar_reporte():
    colaboradores = obtener_colaboradores()
    salarios_brutos, deducciones, salarios_netos = calcular_salarios()

    print ("Reporte de planilla")
    print ("="*30) #multiplica el "=" 30 veces, para hacer un separador 

    for codigo, datos in colaboradores.items():
        nombre = datos ["nombre"]
        salario_bruto = salarios_brutos [codigo]
        deduccion_detalle = deducciones [codigo]
        salario_neto = salarios_netos [codigo]

        print (f"Colaborador: {nombre}")
        print(f"Código: {codigo}")
        print(f"Salario Bruto: {salario_bruto:.2f}") #está para mostrar 2 decimales, si quiere mostrar mas o menos cambiar el 2
        print("Deducciones:")
        for deduccion, monto in deduccion_detalle.items():
            print (f"{deduccion}: {monto:.2f}")
        print (f"Salario neto: {salario_neto:.2f}")
        print ("="*30)

if __name__ == "__main__":
    generar_reporte()