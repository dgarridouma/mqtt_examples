# topic_alias_subscriber.py
import paho.mqtt.client as mqtt

broker = "broker.emqx.io"
topic = "uma/mqtt5/topic/alias/demo"

def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()} (topic: {msg.topic})")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)  # Versión 2 para MQTT 5
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe(topic)
print("Esperando mensajes en", topic)
client.loop_forever()
