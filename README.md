# Introduction 💻

Dans le cadre de mon Master 1 FullStack, et plus particulièrement de l'UE IOT, j'ai dû travailler en mode projet pendant 5 jours sur un `ESP32 Thing` à l'aide de `micropython` afin d'écouter et utiliser les données de divers capteurs

## Choix technologiques 👾

J'ai choisi de travailler avec 2 capteurs et un écran et de faire une interface web dynamique avec le framework `flask` afin d'avoir un affichage intéractif intelligent des divers données des différents capteurs.

référence des capteurs et de l'écran :

```
Capteur de son (Sound sensor v1.6)
Capteur de température et d'humidité (Température&Humidity Sensor V1.1)
Écran OLED 128/32 (0.91`OLED)
```

Pour emettre et recevoir les données de l'`esp32 thing`, j'ai choisi d'utiliser le protocole `MQTT` qui est très utilisé dans le cadre d'émission / récéption de données des IOT.
pour en savoir plus sur le protocole MQTT [MQTT Documentation](https://mqtt.org/).

J'ai choisi de mon coté d'installer un `Broker MQTT` sur un de mes VPS [OVH](https://www.ovhcloud.com/fr/web-hosting/).

pour ma part, c'est un VPS sous distribution `Linux Ubuntu 20.04` voici le tutoriel utilisé pour faire l'installation d'un `broker MQTT`sur un VPS Ubuntu : [MQTT Broker Mosquitto](https://docs.vultr.com/install-mosquitto-mqtt-broker-on-ubuntu-20-04-server)

Une fois le `broker MQTT` installé, vous pouvez alors établir une communication entre vos divers `IOT` très facilement.


## Schéma de fonctionnement 1️⃣

![Alt text](schema/1.png)

## Schéma de câblage des différents capteurs (ESP32-Thing) 2️⃣

![Alt text](schema/2.png)


## Compétences acquises 3️⃣

J'ai pu acquérir des compétences plus `approfondies` en IOT.
Des compétences en `gestion` de projet.
J'ai également appris l'existence du protocole `MQTT` dont je n'avais pas la connaissance.
J'ai également amélioré mes compétences en `administration système`.


## Difficultés rencontrés 4️⃣

Je n'ai personnellement rencontré aucune réelle difficulté, j'avais déjà fait de l'IOT auparavant, je pense n'avoir rencontré aucune difficulté durant ce projet.

