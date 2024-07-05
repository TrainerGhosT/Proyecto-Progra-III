colaboradores = {}

def registrar_colaborador(codigo, nombre, clave, posicion):
    colaboradores[codigo] = {
        'nombre': nombre,
        'clave': clave,
        'posicion': posicion,
        'horas': [0] * 7  # Asumiendo que son 7 días a la semana
    }
    print(f"Colaborador {nombre} registrado con éxito.")

def obtener_colaboradores():
    return colaboradores
