import time
import machine
import ssd1306
import network
import dht
from umqtt.simple import MQTTClient
import _thread

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
TOPIC_ALERT = b"alert"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connexion au Wi-Fi en cours...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    print("Wi-Fi connecté")
    print("Adresse IP:", wlan.ifconfig()[0])

def read_dht():
    pin_dht = machine.Pin(4, machine.Pin.IN)
    dht_sensor = dht.DHT11(pin_dht)
    dht_sensor.measure()
    return dht_sensor.temperature(), dht_sensor.humidity()

def read_sound():
    adc = machine.ADC(machine.Pin(34))
    adc.atten(machine.ADC.ATTN_11DB)
    return adc.read()

def publish_data():
    while True:
        
        
        temperature, humidity = read_dht()
        sound = read_sound()

        print("Temperature: %d°C" % temperature)
        print("Humidity: %d%%" % humidity)
        print("Sound:", sound)
        
        client.publish(TOPIC_TEMP, str("%d" % temperature))
        client.publish(TOPIC_HUMIDITY, str("%d" % humidity))
        client.publish(TOPIC_SOUND, str(sound))
        
        time.sleep(10)

def subscribe_data():
    
    def sub_cb(topic, msg):
        message = msg.decode('utf-8')
        
        # Afficher le message sur l'écran OLED
        oled.fill(0)
        oled.text(message, 0, 0)
        oled.show()
    
    client.set_callback(sub_cb)
    
    try:
        client.subscribe(TOPIC_ALERT)
        
        while True:
            client.wait_msg()
    except OSError as e:
        print("Error:", e)
    finally:
        print("debug")

# Connexion au Wi-Fi
connect_wifi()

client = MQTTClient(CLIENT_ID, MQTT_BROKER)
client.connect()
# Démarrage des threads pour la publication et la souscription MQTT
_thread.start_new_thread(publish_data, ())
_thread.start_new_thread(subscribe_data, ())
