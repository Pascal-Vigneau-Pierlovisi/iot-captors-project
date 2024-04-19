from machine import ADC, Pin
import time

# Initialisation de la pin ADC
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)  # Configurer l'atténuation pour une plage complète de 0-3.3V

while True:
    valeur = adc.read()  # Lire la valeur analogique
    print("Valeur du capteur de son :", valeur)
    time.sleep(3)  # Temporisation de 100 ms entre les lectures
