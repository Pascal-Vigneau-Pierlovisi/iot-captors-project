from umqtt.simple import MQTTClient
import time
import ssd1306
import machine


# Configuration des broches SCL et SDA
scl_pin = machine.Pin(22)  # Définissez la broche SCL
sda_pin = machine.Pin(21)  # Définissez la broche SDA

# Configuration de l'écran OLED
oled_width = 128  # Largeur de l'écran OLED en pixels
oled_height = 32  # Hauteur de l'écran OLED en pixels
i2c = machine.I2C(scl=scl_pin, sda=sda_pin)
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


# Configuration Wi-Fi
WIFI_SSID = "pascal"
WIFI_PASSWORD = "Legoal2C"

# Configuration MQTT
MQTT_BROKER = "37.187.180.19"
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


# Fonction de souscription aux données MQTT
def subscribe_data():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER)
    
    # Définir le callback de souscription
    def sub_cb(topic, msg):
        # Efface l'écran OLED
        oled.fill(0)
        oled.show()
        
        # Affichage des données sur l'écran OLED
        if topic == TOPIC_TEMP:
            oled.text("T : " + str(msg), 0, 0)
        elif topic == TOPIC_HUMIDITY:
            oled.text("H : " + str(msg), 0, 10)
        elif topic == TOPIC_SOUND:
            oled.text("S : " + str(msg), 0, 20)
        
        oled.show()
    
    # Définir le callback de souscription pour le client MQTT
    client.set_callback(sub_cb)
    
    # Connexion au broker MQTT
    client.connect()
    
    # Souscription aux sujets
    client.subscribe(TOPIC_TEMP)
    client.subscribe(TOPIC_HUMIDITY)
    client.subscribe(TOPIC_SOUND)
    
    # Boucle de gestion des messages MQTT
    while True:
        client.wait_msg()
        
    # Déconnexion du client MQTT
    client.disconnect()


# Connexion au Wi-Fi
connect_wifi()

# Souscription aux données MQTT
subscribe_data()
