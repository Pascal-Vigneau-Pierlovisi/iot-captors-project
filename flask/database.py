import mysql.connector

# Configuration de la base de données MySQL
db_config = {
    'host': 'localhost',
    'user': 'mqtt',
    'port' : '8889',
    'password': 'your_password',
    'database': 'sensor_db'
}

# Fonction pour établir une connexion à la base de données
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    print(connection.is_connected())
    return connection