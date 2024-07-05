from registros.colaboradores import obtener_colaboradores

def registrar_horas(codigo, dia, horas_trabajadas):
    colaboradores = obtener_colaboradores()
    if codigo in colaboradores:
        colaboradores[codigo]['horas'][dia] = horas_trabajadas
        print(f"Horas registradas para el colaborador {colaboradores[codigo]['nombre']}.")
    else:
        print("Código de colaborador no encontrado.")
