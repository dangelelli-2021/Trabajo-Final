

# Funcion que recibe la lista de diccionarios crudos, los recorre y los devuelve limpios

def limpiar_registro_sensor(diccionario):

    dicc_limpio = []

    for sensor in diccionario:
        # Quitar todos los espacios en blanco del sensor_id
        id_limpio = sensor["sensor_id"].replace(" ", "")
    
        # Dejar solo el valor float en la temperatura (quitando espacios y la 'C')
        temp_sucia = sensor["temperatura"].replace(" ", "").upper()
        temp_limpia = float(temp_sucia.replace("C", ""))
    
        # Validar la ubicación y rellenar si está vacía
        ubicacion_sucia = sensor["ubicacion"].strip()
        ubicacion_limpia = ubicacion_sucia if ubicacion_sucia != "" else "No-definida"
    
        # Construir el nuevo diccionario
        nuevo_sensor = {
            "sensor_id": id_limpio,
            "temperatura": temp_limpia,
            "ubicacion": ubicacion_limpia
        }
    
        dicc_limpio.append(nuevo_sensor)
    return(dicc_limpio)

# Funcion que permite seleccionar los sensores que superan el umbral y sacar el promedio de temperatura total de todos.

def generar_resumen_sensores(DiccLimpio, TempMax:float):

    lista_sensores_alerta = []
    contador = 0
    prom_temp = 0
    
    for sensor in DiccLimpio:
        # 
        contador += 1
        prom_temp = prom_temp + sensor["temperatura"]   
            
        # Construir la lista con temperaturas superiores a la Maxima
        if sensor["temperatura"] > TempMax:
            lista_sensores_alerta.append(sensor["sensor_id"])
            
    # Calculo temperatura promedio
    prom_temp = prom_temp / contador

    # Armado de la tupla solicitada y posterior retorno

    tupla_con_promedio = ([lista_sensores_alerta] , prom_temp)
    
    return (tupla_con_promedio)
        
# Lista de diccionarios de ejemplo para pruebas

dicc = [
    { "sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte" },
    { "sensor_id": " SENSOR-002 ", "temperatura": "28", "ubicacion": "Planta Sur" },
    { "sensor_id": " SE NSOR-003 ", "temperatura": "24.5", "ubicacion": "" },
    { "sensor_id": " SENSOR-004 ", "temperatura": "28.5C ", "ubicacion": "Planta" }
]

# LLamada a funcion para limpiar todos los diccionarios de la lista

dicc_limpio = limpiar_registro_sensor(dicc)

# Mostrar la lista con diccionarios limpios
print("-" * 80)
print ("Lista de diccionarios sanitizados:" )
print("-" * 80)
print(*dicc_limpio, sep="\n")
print("-" * 80)

#Solicitud de umbral de temperatura al usuario

temp_limite = float(input ("Ingrese valor de temperatura límite:"))

print("-" * 60)

# Mostrar la tupla con lista_sensores_alerta y promedio_temperatura

tupla_final = generar_resumen_sensores(dicc_limpio , temp_limite)

print(f"Lista de IDs de los sensores que superan el umbral estipulado: {tupla_final[0]}")

print("-" * 60)

print(f"Promedio térmico global de la planta: {tupla_final[1]}")

print("-" * 60)

      


