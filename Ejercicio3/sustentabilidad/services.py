
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """
    Calcula las emisiones de carbono a partir del consumo kwh.
    Eleva ValueError si el consumo es negativo
    """
    #Agregar sugerencia de tipo

    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    return consumo_kwh * factor_emision

def obtener_metricas_consumo(registros):
    """
    Obtiene las metricas de consumo
    """
    total_global_emisiones = 0.0
    emisiones_por_planta = {}
    planta_mayor_consumo = None
    mayor_emision = -1

    for registro in registros:
        planta = registro.get("planta", "Planta desconocida")
        consumo = registro.get("consumo_kwh", 0.0)

        emisiones = calcular_emisiones_carbono(consumo)
        total_global_emisiones += emisiones

        if planta not in emisiones_por_planta:
            emisiones_por_planta[planta] = 0.0
        emisiones_por_planta[planta] += emisiones 

    for planta, emisiones in emisiones_por_planta.items():
        if emisiones > mayor_emision:
            mayor_emision = emisiones
            planta_mayor_consumo = planta

    return {
        "total_global_emisiones": total_global_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "emisiones_por_planta": emisiones_por_planta
    }
                   

registro_historicos = [
    {'planta':'Planta Norte', 'consumo_kwh': 1200.0},
    {'planta':'Planta Sur', 'consumo_kwh': 3400.50},
    {'planta':'Planta Este', 'consumo_kwh': 850.2},
    {'planta':'Planta Oeste', 'consumo_kwh': 2100.0},
    {'planta':'Planta Norte', 'consumo_kwh': 200.0},
]       

