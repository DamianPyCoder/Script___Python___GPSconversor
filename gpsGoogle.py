import googlemaps
gmaps = googlemaps.Client(key='TU_CLAVE_DE_API')

def obtener_direccion(latitud, longitud):
    resultado = gmaps.reverse_geocode((latitud, longitud))
    if resultado:
        direccion = resultado[0]['formatted_address']
        return direccion
    else:
        return "No se pudo encontrar la dirección."

latitud = 37.7749  # Ejemplo de latitud
longitud = -122.4194  # Ejemplo de longitud

direccion = obtener_direccion(latitud, longitud)
print("La dirección es:", direccion)
