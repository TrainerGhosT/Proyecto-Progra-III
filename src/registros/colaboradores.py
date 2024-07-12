colaboradores = {}

def registrar_colaborador(codigo, nombre, clave, posicion):
    if codigo in colaboradores:
        print(f"El código {codigo} ya está registrado.")
        return
    colaboradores[codigo] = {
        'nombre': nombre,
        'clave': clave,
        'posicion': posicion,
        'horas': [0] * 6  # Asumiendo que son 6 días a la semana (lunes a sábado)
    }
    print(f"Colaborador {nombre} registrado con éxito.")

def obtener_colaboradores():
    return colaboradores
