import paho.mqtt.client as mqtt
import mysql.connector
from mysql.connector import Error
import time

# Database connection
try:
    connection = mysql.connector.connect(
        host='localhost',       # Your MySQL server host
        port = '8889',
        user='mqtt',            # Your MySQL username
        password='your_password',    # Your MySQL password
        database='sensor_db'    # Your database name
    )
except Error as e:
    print("Error connecting to MySQL database", e)
    exit(1)

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("iot/plt/temp")  # The topic you want to subscribe to
    client.subscribe("iot/plt/humidity")  # The topic you want to subscribe to
    client.subscribe("iot/plt/sound")  # The topic you want to subscribe to

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    cursor = connection.cursor()
    try:
        query = "INSERT INTO sensor_data (topic, payload) VALUES (%s, %s)"
        cursor.execute(query, (msg.topic, msg.payload.decode()))
        connection.commit()
    except Error as e:
        print("Failed to insert data into MySQL table", e)
    finally:
        cursor.close()

# MQTT Client setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Set this if your MQTT broker requires authentication
client.connect("localhost", 1883, 6000)  # Connect to the MQTT broker

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()
