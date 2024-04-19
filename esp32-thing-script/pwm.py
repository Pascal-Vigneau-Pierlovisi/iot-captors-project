from machine import Pin, PWM
import time

ledPin = Pin(5, Pin.OUT)
pwm = PWM(ledPin)

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    input_value = int(input("Entrez une valeur entre 0 et 1023 : "))  # Supposons que la valeur d'entrée provient d'un capteur analogique
    pwm_value = int(map_value(input_value, 0, 1023, 0, 1023))
    pwm.duty(pwm_value)
    print("Valeur PWM réglée :", pwm_value)
    time.sleep(0.5)
