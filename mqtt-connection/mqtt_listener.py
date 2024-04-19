import paho.mqtt.client as mqtt
import mysql.connector
from mysql.connector import Error
import time

# Database connection
try:
    connection = mysql.connector.connect(
        host='localhost',       # Your MySQL server host
        port='8889',
        user='mqtt',            # Your MySQL username
        password='your_password',    # Your MySQL password
        database='sensor_db'    # Your database name
    )
except Error as e:
    print("Error connecting to MySQL database", e)
    exit(1)

# Function to check and adjust table size
def adjust_table_size(topic):
    cursor = connection.cursor()
    table_name = "sensor_" + topic
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    if count >= 30:
        delete_query = f"DELETE FROM {table_name} ORDER BY id LIMIT 1"
        cursor.execute(delete_query)
        connection.commit()
    cursor.close()

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("temp")  # The topic you want to subscribe to
    client.subscribe("humidity")  # The topic you want to subscribe to
    client.subscribe("sound")  # The topic you want to subscribe to

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    cursor = connection.cursor()
    try:
        adjust_table_size(msg.topic)
        table_name = "sensor_" + msg.topic
        query = f"INSERT INTO {table_name} (topic, payload) VALUES (%s, %s)"
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
client.connect("37.187.180.19", 1883, 6000)  # Connect to the MQTT broker

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()
