# Importation des modules nécessaires
import machine
import ssd1306
import time

# Configuration des broches SCL et SDA
scl_pin = machine.Pin(22)  # Définissez la broche SCL
sda_pin = machine.Pin(21)  # Définissez la broche SDA

# Configuration de l'écran OLED
oled_width = 128  # Largeur de l'écran OLED en pixels
oled_height = 32  # Hauteur de l'écran OLED en pixels
i2c = machine.I2C(scl=scl_pin, sda=sda_pin)
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Efface l'écran OLED
oled.fill(0)
oled.show()

# Affiche du texte sur l'écran OLED
oled.text("Bonjour !", 0, 0)
oled.text("C'est un test", 0, 10)
oled.text("d'écran OLED", 0, 20)
oled.show()

# Attendez quelques secondes avant d'éteindre l'écran
time.sleep(5)

# Efface l'écran OLED
oled.fill(0)
oled.show()

