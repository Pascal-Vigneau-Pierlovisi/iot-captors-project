import machine
import time

# Configuration des broches RX et TX
RX_PIN = 16  # Broche RX de l'ESP32 Thing
TX_PIN = 17  # Broche TX de l'ESP32 Thing

# Initialiser la liaison série
uart = machine.UART(1, baudrate=9600, tx=RX_PIN, rx=TX_PIN)

while True:
    # Attendre la réception de données depuis le module NFC
    if uart.any():
        # Lire les données reçues depuis le module NFC
        nfc_data = uart.read()

        # Afficher les données lues
        print("Données NFC reçues:", nfc_data)

    # Attendre un court laps de temps avant de vérifier à nouveau
    time.sleep(0.1)
