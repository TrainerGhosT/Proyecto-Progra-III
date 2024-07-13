from registros.colaboradores import obtener_colaboradores

SALARIO_POR_HORA = 4500
HORAS_ORDINARIAS = 4
BONO_HORA_EXTRA = 1.5

def calcular_salarios():
    colaboradores = obtener_colaboradores()
    salarios_brutos = {}
    deducciones = {}
    salarios_netos = {}

    for codigo, datos in colaboradores.items():
        horas = datos['horas']

        #calculo horas ordinarias, extraordinarias y salario bruto
        horas_ordinarias = sum(min(h, HORAS_ORDINARIAS) for h in horas)
        horas_extras = sum(max(0, h - HORAS_ORDINARIAS) for h in horas)
        salario_bruto = (horas_ordinarias * SALARIO_POR_HORA) + (horas_extras * SALARIO_POR_HORA * BONO_HORA_EXTRA)

        #deducciones y salario neto
        deduccion_ccss = salario_bruto * 0.055
        deduccion_ivm = salario_bruto * 0.035
        deduccion_bp = salario_bruto * 0.01
        total_deducciones = deduccion_ccss + deduccion_ivm + deduccion_bp
        salario_neto = salario_bruto - total_deducciones

        #diccionario para guardar la info de las deducciones
        salarios_brutos[codigo] = salario_bruto
        deducciones[codigo] = {
            'CCSS': deduccion_ccss,
            'IVM': deduccion_ivm,
            'BP': deduccion_bp
        }
        salarios_netos[codigo] = salario_neto

    return salarios_brutos, deducciones, salarios_netos
