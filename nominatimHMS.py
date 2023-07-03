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

# Ejemplo de uso
grados_lat = 41
minutos_lat = 23
segundos_lat = 30

grados_lon = 2
minutos_lon = 10
segundos_lon = 15

direccion = obtener_direccion(grados_lat, minutos_lat, segundos_lat, grados_lon, minutos_lon, segundos_lon)
print("La dirección es:", direccion)
