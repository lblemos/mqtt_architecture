import paho.mqtt.client as mqtt 
import time

class device:
    def __init__(self, device_name, mqtt_client, mqtt_topic, mqtt_broker):
        
        self.device_name = device_name
        self.mqtt_client = mqtt_client 
        self.mqtt_topic = mqtt_topic
        self.mqtt_broker = mqtt_broker 

        pass

    def send(self, qtd):

        client = mqtt.Client(self.mqtt_client)
        client.connect(self.mqtt_broker)



        device = self.device_name
        id = 1

        while id <= qtd:
            msg = device + str(id)
            client.publish(self.mqtt_topic, msg)
            print("Just published id " + str(id) +" "+ device)
            time.sleep(0.01)
            id += 1

    