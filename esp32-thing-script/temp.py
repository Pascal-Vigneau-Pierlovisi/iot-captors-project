import dht
from machine import Pin, ADC
import time

# Définir le GPIO auquel le capteur est connecté
pin_dht = Pin(4, Pin.IN)

# Créer un objet DHT11
dht_sensor = dht.DHT11(pin_dht)

# Initialisation de la pin ADC
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)  # Configurer l'atténuation pour une plage complète de 0-3.3V

# Configuration du capteur de son

while True:
    # Lire les données du capteur de température et d'humidité
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    
    # Afficher les données de température et d'humidité
    print("Temperature: %d°C" % temperature)
    print("Humidity: %d%%" % humidity)
    
    valeur = adc.read()  # Lire la valeur analogique
    print("Valeur du capteur de son :", valeur)
    time.sleep(3)  # Temporisation de 100 ms entre les lectures
    
    # Lecture des données du capteur de son

    
    # Attendre quelques secondes avant la prochaine lecture
    time.sleep(2)
    
    

    


