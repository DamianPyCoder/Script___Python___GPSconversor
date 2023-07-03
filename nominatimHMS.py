import requests

def convertir_coordenadas(grados, minutos, segundos):
    # Convertir las coordenadas a formato decimal
    coordenadas_decimal = grados + minutos/60 + segundos/3600
    return coordenadas_decimal

def obtener_direccion(grados_lat, minutos_lat, segundos_lat, grados_lon, minutos_lon, segundos_lon):
    latitud = convertir_coordenadas(grados_lat, minutos_lat, segundos_lat)
    longitud = convertir_coordenadas(grados_lon, minutos_lon, segundos_lon)

    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitud}&lon={longitud}&zoom=18&addressdetails=1"
    respuesta = requests.get(url).json()
    
    if 'error' in respuesta:
        return "No se pudo obtener la dirección."
    
    direccion = respuesta['address']
    calle = direccion.get('road', '')
    numero = direccion.get('house_number', '')
    
    return f"Calle: {calle}, Número: {numero}"

# Solicitar coordenadas al usuario
grados_lat = float(input("Introduce los grados de latitud: "))
minutos_lat = float(input("Introduce los minutos de latitud: "))
segundos_lat = float(input("Introduce los segundos de latitud: "))

grados_lon = float(input("Introduce los grados de longitud: "))
minutos_lon = float(input("Introduce los minutos de longitud: "))
segundos_lon = float(input("Introduce los segundos de longitud: "))

# Obtener dirección y mostrar el resultado
direccion = obtener_direccion(grados_lat, minutos_lat, segundos_lat, grados_lon, minutos_lon, segundos_lon)
print("La dirección es:", direccion)

