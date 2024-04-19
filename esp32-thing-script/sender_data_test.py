import time
from umqtt.simple import MQTTClient
from machine import Pin, ADC
import dht

# Configuration Wi-Fi
WIFI_SSID = "your_ssid"
WIFI_PASSWORD = "your_password"

# Configuration MQTT
MQTT_BROKER = "your_broker_ip"
CLIENT_ID = "ESP32_Client"
CLIENT_USER = "your_username"
CLIENT_PASS = "your_password"

TOPIC_TEMP = b"iot/plt/temp"
TOPIC_HUMIDITY = b"iot/plt/humidity"
TOPIC_SOUND = b"iot/plt/sound"

# Fonction de connexion au Wi-Fi
def connect_wifi():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connexion au Wi-Fi en cours...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    print("Wi-Fi connecté")
    print("Adresse IP:", wlan.ifconfig()[0])

# Fonction de lecture de température et d'humidité
def read_dht():
    pin_dht = Pin(4, Pin.IN)
    # Créer un objet DHT11
    dht_sensor = dht.DHT11(pin_dht)
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    return temperature, humidity

# Fonction de lecture du son
def read_sound():
    adc = ADC(Pin(34))
    adc.atten(ADC.ATTN_11DB)  # Configurer l'atténuation pour une plage complète de 0-3.3V
    return adc.read()

# Fonction de publication des données MQTT
def publish_data():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, port=1883, user=CLIENT_USER, password=CLIENT_PASS)
    client.connect()
    
    temperature, humidity = read_dht()
    sound = read_sound()
    
    print("Temperature: %d°C" % temperature)
    print("Humidity: %d%%" % humidity)
    print("Son:", sound)
    
    client.publish(TOPIC_TEMP, str("%d" % temperature))
    client.publish(TOPIC_HUMIDITY, str("%d" % humidity))
    client.publish(TOPIC_SOUND, str(sound))
    
    client.disconnect()

# Connexion au Wi-Fi
connect_wifi()

# Boucle principale
while True:
    publish_data()
    time.sleep(2) # Attendre 5 secondes avant de publier de nouveau

