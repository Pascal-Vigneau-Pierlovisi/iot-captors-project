from machine import Pin
import time

# Configuration du GPIO pour contrôler le ventilateur
ventilateur_pin = Pin(12, Pin.OUT)

# Fonction pour définir une vitesse fixe pour le ventilateur
def regler_vitesse_fixe(vitesse):
    if vitesse < 0:
        vitesse = 0
    elif vitesse > 100:
        vitesse = 100

    # Convertir la valeur de vitesse de 0-100 à une valeur de 0-1 pour la durée active
    temps_actif = vitesse / 100.0

    # Allumer le ventilateur pendant la durée définie pour la vitesse
    ventilateur_pin.on()
    time.sleep(temps_actif)

# Définir une vitesse fixe de 50%
regler_vitesse_fixe(50)
