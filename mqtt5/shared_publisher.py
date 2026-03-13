import paho.mqtt.client as mqtt
import time

broker = "broker.emqx.io"
#broker = "localhost"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)

client.connect(broker, 1883)

for i in range(1, 6):  # Publica 5 mensajes
    client.publish("uma/mqtt5/shared", f"Mensaje {i}")
    print(f"Publicado: Mensaje {i}")
    time.sleep(1)

client.disconnect()
