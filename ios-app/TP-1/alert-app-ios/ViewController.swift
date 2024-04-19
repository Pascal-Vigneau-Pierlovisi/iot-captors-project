import UIKit
import LightMQTT

class ViewController: UIViewController {
    
    var mqttClient: LightMQTT?

    override func viewDidLoad() {
        super.viewDidLoad()

        // Configurer les options du client MQTT avec LightMQTT
        var options = LightMQTT.Options()
        options.clientId = "iOSClient_01"
        options.pingInterval = 60
        options.bufferSize = 4096
        options.readQosClass = .background

        mqttClient = LightMQTT(host: "37.187.180.19", options: options)

        // Demander les autorisations de notification
        UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge]) { granted, error in
            // Gérer les autorisations
        }

        // Connecter et configurer les souscriptions
        mqttClient?.connect() { success in
            if success {
                self.mqttClient?.subscribe(to: "alert")
                
                // Configuration de la réception des messages
                self.mqttClient?.receivingMessage = { topic, message in
                    DispatchQueue.main.async {
                        self.displayNotification(for: message)
                    }
                }
            }
        }
    }

    private func displayNotification(for message: String) {
        let notificationContent = UNMutableNotificationContent()
        notificationContent.title = "Alerte !"
        notificationContent.body = message
        notificationContent.sound = UNNotificationSound(named: UNNotificationSoundName(rawValue: "ca-va-peter_nR3IwZJ.m4a"))
        
        let request = UNNotificationRequest(identifier: "mqttNotification", content: notificationContent, trigger: nil)
        UNUserNotificationCenter.current().add(request, withCompletionHandler: nil)
    }
    
    deinit {
        mqttClient?.disconnect()
    }
}
