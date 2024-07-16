from registros.colaboradores import obtener_colaboradores

def calcular_horasTrabajadas(entrada, salida):
        try:
            #extraer dos numeros
            entrada_horas = int(entrada[:2])
            entrada_minutos = int(entrada[2:])
            salida_horas = int(salida[:2])
            salida_minutos = int(salida[2:])

            if not (0<= entrada_horas < 24 and 0 <= entrada_minutos < 60 and 0 <= salida_horas <24 and 0 <+ salida_minutos <60):
                raise ValueError ("Formato de hora incorrecto, Use HHMM (ejemplo 0800 para 8AM)")

            total_entrada = entrada_horas*60 + entrada_minutos
            total_salida = salida_horas*60 + salida_minutos

            if total_salida < total_entrada:
                raise ValueError ("La hora de salida no puede ser anterior a la entrada")

            #calcular los min y convertir a horas
            total_minutosTrabajados = total_salida - total_entrada
            horas_trabajadas = total_minutosTrabajados/60.0
            return horas_trabajadas
        
        except Exception as ex:
            raise ValueError (f"Error al calcular las horas trabajadas:{ex}")
        
def registrar_horas(codigo, dia, entrada, salida):
    colaboradores = obtener_colaboradores()
    if codigo in colaboradores:
        try:
            horas_trabajadas = calcular_horasTrabajadas(entrada, salida)
            colaboradores[codigo]["horas"][dia] = horas_trabajadas
            print(f"Horas registradas para {colaboradores[codigo]['nombre']}")
        except ValueError as ex:
            
            print(f"Error en el calculo de horas {ex}")
    else:
        print("Código de colaborador no encontrado.")
        return
