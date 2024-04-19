from machine import Pin
import time

ledPin = Pin(5, Pin.OUT)

value = float(input('Valeur : '))

while True:
    ledPin.on()
    time.sleep(value)
    ledPin.off()
    time.sleep(value)
