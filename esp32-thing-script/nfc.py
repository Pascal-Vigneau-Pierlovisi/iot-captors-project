import machine

# Initialiser UART avec les broches GPIO
uart = machine.UART(1, baudrate=115200, tx=16, rx=17)

def main():
    print("Attente d'un tag NFC...")
    while True:
        if uart.any():
            uid = uart.read()
            print("Tag NFC trouvé!")
            print("UID: ", uid)
            # Ajoutez ici votre code pour traiter les données du tag NFC
            break  # Sortir de la boucle une fois qu'un tag NFC est trouvé

if __name__ == "__main__":
    main()
