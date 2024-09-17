import time
import requests
from geopy.geocoders import Nominatim

# Configuración
BOT_TOKEN = 'TU_TOKEN_DE_TELEGRAM'  # Reemplaza con tu token de Telegram
CHAT_ID = 'TU_CHAT_ID'              # Reemplaza con tu chat ID
INTERVALO_ENVIO = 60                # Intervalo de envío en segundos

def obtener_ubicacion():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("Tu dirección exacta")  # O usa una posición fija si no tienes GPS
    return location.latitude, location.longitude

def enviar_ubicacion(lat, lon):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendLocation"
    params = {
        'chat_id': CHAT_ID,
        'latitude': lat,
        'longitude': lon
    }
    requests.get(url, params=params)

def main():
    while True:
        lat, lon = obtener_ubicacion()
        enviar_ubicacion(lat, lon)
        time.sleep(INTERVALO_ENVIO)

if __name__ == "__main__":
    main()
