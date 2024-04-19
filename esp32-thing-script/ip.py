import network

def get_ip():
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.active():
        return sta_if.ifconfig()[0]
    else:
        return None

ip_address = get_ip()
if ip_address:
    print("Adresse IP de l'ESP32:", ip_address)
else:
    print("L'interface Wi-Fi de l'ESP32 n'est pas activée.")
