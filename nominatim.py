import requests

def obtener_direccion(latitud, longitud):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitud}&lon={longitud}&zoom=18&addressdetails=1"
    respuesta = requests.get(url).json()
    
    if 'error' in respuesta:
        return "No se pudo obtener la dirección."
    
    direccion = respuesta['address']
    calle = direccion.get('road', '')
    numero = direccion.get('house_number', '')
    
    return f"Calle: {calle}, Número: {numero}"

# Ejemplo de uso
latitud = 41.3851  # Ejemplo de latitud (Barcelona)
longitud = 2.1734  # Ejemplo de longitud (Barcelona)

direccion = obtener_direccion(latitud, longitud)
print("La dirección es:", direccion)
