from registros.colaboradores import obtener_colaboradores

def registrar_horas(codigo, dia, horas_trabajadas):
    colaboradores = obtener_colaboradores()
    if codigo not in colaboradores:
        print("Código de colaborador no encontrado.")
        return
    if dia < 0 or dia >= 6:
        print("Día inválido. Debe estar entre 0 (lunes) y 5 (sábado).")
        return
    if horas_trabajadas < 0 or horas_trabajadas > 8:
        print("Horas trabajadas inválidas. Deben estar entre 0 y 8.")
        return
    colaboradores[codigo]['horas'][dia] = horas_trabajadas
    print(f"Horas registradas para el colaborador {colaboradores[codigo]['nombre']}.")

