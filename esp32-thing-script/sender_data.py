import time
from umqtt.simple import MQTTClient
from machine import Pin, ADC
import machine
import dht
import ssd1306

# Configuration des broches SCL et SDA
scl_pin = machine.Pin(22)  # Définissez la broche SCL
sda_pin = machine.Pin(21)  # Définissez la broche SDA

# Configuration de l'écran OLED
oled_width = 128  # Largeur de l'écran OLED en pixels
oled_height = 32  # Hauteur de l'écran OLED en pixels
i2c = machine.I2C(scl=scl_pin, sda=sda_pin)
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


# Configuration Wi-Fi
WIFI_SSID = "your_ssid"
WIFI_PASSWORD = "your_password"

# Configuration MQTT
MQTT_BROKER = "your_broker_ip"
CLIENT_ID = "ESP32_Client"
TOPIC_TEMP = b"temp"
TOPIC_HUMIDITY = b"humidity"
TOPIC_SOUND = b"sound"

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

def read_sound():
    adc = ADC(Pin(34))
    adc.atten(ADC.ATTN_11DB)  # Configurer l'atténuation pour une plage complète de 0-3.3V
    
    # Collecte des mesures pendant 20 ms
    start_time = time.ticks_ms()
    values = []
    while time.ticks_diff(time.ticks_ms(), start_time) < 20:
        values.append(adc.read())
    
    
    # Calcul de la moyenne des mesures
    if values:
        avg_value = sum(values) / len(values)
    else:
        avg_value = 0
    
    return avg_value

# Fonction de publication des données MQTT
def publish_data():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER)
    client.connect()
    
    temperature, humidity = read_dht()
    sound = read_sound()
    
    # Efface l'écran OLED
    oled.fill(0)
    oled.show()
    oled.text("T : " + str(temperature), 0, 0)
    oled.text("H : " + str(humidity), 0, 10)
    oled.text("S : " + str(sound) , 0, 20)
    oled.show()
    
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
