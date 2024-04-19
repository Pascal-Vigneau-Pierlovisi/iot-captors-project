from flask import Flask, render_template, request, redirect, url_for, session, send_file, Response, make_response, jsonify
from database import get_db_connection
import hashlib
import plotly.graph_objs as go
from datetime import datetime
import time
import paho.mqtt.publish as publish


app = Flask(__name__)
app.secret_key = '6bfc8de466585b910041545eba2bb2b5'
db = get_db_connection()


"""
La fonction index() est une vue qui affiche la page d'accueil.
"""
@app.route("/")
def index():
    return render_template('index.html')

"""
La fonction showRegister() est une vue qui affiche le formulaire d'inscription.
"""
@app.route('/register', methods=['GET'])
def showRegister():
    if(session.get('user_id')):
        return redirect(url_for('index'))
    else:
        return render_template('register.html')

"""
La fonction register() est une vue qui gère la soumission du formulaire d'inscription.
Elle vérifie si les mots de passe correspondent, puis traite les données d'inscription.
Si les mots de passe ne correspondent pas, un message d'erreur est affiché.
@method POST
"""
@app.route('/register', methods=['POST'])
def register():

    if(session.get('user_id')):
        return redirect(url_for('index'))
    else:
        # Récupérer les données du formulaire
        username = request.form['username']
        password = request.form['password']
        password_confirm = request.form['password_confirm']

        # Vérifier si les mots de passe correspondent
        if password != password_confirm:
            error_message = "Les mots de passe ne correspondent pas. Veuillez réessayer."
            return render_template('register.html', error_message=error_message)

        # Vérifier si l'utilisateur existe déjà
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        user_exists = cursor.fetchone()
        cursor.close()

        if user_exists:
            error_message = "Cet utilisateur existe déjà. Veuillez choisir un autre nom d'utilisateur."
            return render_template('register.html', error_message=error_message)

        # Chiffrer le mot de passe avant de l'enregistrer dans la base de données
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Insérer le nouvel utilisateur dans la base de données
        cursor = db.cursor()
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        cursor.close()

        success_message = "Inscription réussie! Vous pouvez maintenant vous connecter."
        return render_template('register.html', success_message=success_message)

"""
La fonction login() est une vue qui gère la soumission du formulaire de connexion.
"""
@app.route('/login', methods=['GET'])
def showLogin():
    if(session.get('user_id')):
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

"""
La fonction login() est une vue qui gère la soumission du formulaire de connexion.
Elle vérifie si l'utilisateur existe et si le mot de passe correspond.
Si les informations d'identification sont correctes, l'utilisateur est connecté.
"""
@app.route('/login', methods=['POST'])
def login():
    if(session.get('user_id')):
        return redirect(url_for('index'))
    
    else:
        # Récupérer les données du formulaire
        username = request.form['username']
        password = request.form['password']

        # Récupérer l'utilisateur depuis la base de données
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()

        # Vérifier si l'utilisateur existe et si le mot de passe correspond
        if user and user['password'] == hashlib.sha256(password.encode()).hexdigest():
            # Définir une variable de session pour l'identifiant de l'utilisateur
            session['user_id'] = user['id']
            # Ici, nous supposons que vous avez déjà implémenté la gestion des sessions Flask

            # Rediriger vers une page de succès ou une autre page après la connexion
            return redirect(url_for('index'))
        else:
            # Si les informations d'identification sont incorrectes, afficher un message d'erreur
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render_template('login.html', error_message=error_message)
    
"""
La fonction logout() est une vue qui gère la déconnexion de l'utilisateur.
Elle supprime la variable de session de l'identifiant de l'utilisateur et redirige vers la page de connexion.
"""
@app.route('/logout')
def logout():
    if(session.get('user_id')):
        session.pop('user_id', None)
        return redirect(url_for('login'))
    else: 
        return redirect(url_for('index'))

"""
La fonction gestion_json() est une vue qui renvoie les données des 30 derniers enregistrements pour les capteurs de température, d'humidité et de son.
Elle renvoie les données au format JSON pour être utilisées dans une application frontale.
"""
@app.route('/gestion/json')
def gestion_json():
    if session.get('user_id'):
        last_30_temp = get_last_30_records('temp')
        last_30_humidity = get_last_30_records('humidity')
        last_30_sound = get_last_30_records('sound')

        last_temp = last_30_temp[-1]['payload'] if last_30_temp else None
        last_humidity = last_30_humidity[-1]['payload'] if last_30_humidity else None
        last_sound = last_30_sound[-1]['payload'] if last_30_sound else None

        return jsonify({
            "last_temp": last_temp,
            "last_humidity": last_humidity,
            "last_sound": last_sound,
            "temp_data": last_30_temp,
            "humidity_data": last_30_humidity,
            "sound_data": last_30_sound,
            "time": datetime.now().strftime('%H:%M:%S')
        })
    else:
        return jsonify({"error": "User not authenticated"}), 401

"""
La fonction gestion() est une vue qui affiche la page de gestion des capteurs.
Elle vérifie si l'utilisateur est connecté, puis affiche la page de gestion.
Si l'utilisateur n'est pas connecté, il est redirigé vers la page de connexion.
"""
@app.route('/gestion')
def gestion():
    if session.get('user_id'):
        return render_template('gestion.html')
    else:
        return redirect(url_for('login'))

"""
La fonction send_alert() est une vue qui envoie une alerte à un broker MQTT.
Elle récupère le message à envoyer depuis la requête JSON, puis l'envoie sur le topic spécifié.
"""
@app.route("/send_alert", methods=["POST"])
def send_alert():
    # Configuration du broker MQTT
    MQTT_BROKER = "your_broker_ip"
    MQTT_PORT = 1883
    MQTT_TOPIC = "alert"
    try:
 
        # Récupérer le message à envoyer depuis la requête JSON
        data = request.json
        message = data["message"]
        print(data['message'])

        # Envoyer le message MQTT sur le topic spécifié
        publish.single(MQTT_TOPIC, message, hostname=MQTT_BROKER, port=MQTT_PORT)

        return jsonify({"success": True, "message": "Alerte envoyée avec succès"}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

"""
La fonction get_last_30_records() récupère les 30 derniers enregistrements pour un topic donné depuis la base de données.
Elle renvoie une liste d'objets représentant les enregistrements récupérés.
"""
def get_last_30_records(topic):
    """
    Récupère les 30 derniers enregistrements pour un topic donné depuis la base de données.
    Args:
        topic (str): Le nom du topic pour lequel récupérer les données (temp, humidity, sound, etc.).
    Returns:
        list: Une liste d'objets représentant les enregistrements récupérés.
    """
    table_name = "sensor_" + topic
    cursor = db.cursor(dictionary=True)

    try:
        # Exécutez la requête pour récupérer les données
        query = f"SELECT * FROM {table_name} WHERE topic = %s"
        cursor.execute(query, (topic,))
        records = cursor.fetchall()

        # Reformatez les dates
        for record in records:
            record['received_at'] = datetime.strftime(record['received_at'], '%H:%M')

        # Affichage du dernier élément de la liste
        if records:
            print("Dernier enregistrement récupéré :", records[-1])
        else:
            print("Aucun enregistrement trouvé.")
            
        return records
        
    except Error as e:
        print("Error fetching data from MySQL table:", e)
    
    finally:
        # Fermez le curseur et réouvrez la connexion
        cursor.close()
        db.reconnect()


    try:
        # Récupérer le message à envoyer depuis la requête JSON
        data = request.json
        message = data["message"]

        # Envoyer le message MQTT sur le topic spécifié
        publish.single(MQTT_TOPIC, message, hostname=MQTT_BROKER, port=MQTT_PORT)

        return jsonify({"success": True, "message": "Alerte envoyée avec succès"}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500