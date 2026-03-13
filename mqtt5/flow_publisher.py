# publisher_fast.py
import time
import paho.mqtt.client as mqtt

broker = "broker.emqx.io"
topic = "uma/mqtt5/flowcontrol"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
client.connect(broker, 1883)
client.loop_start()

for i in range(10):
    client.publish(topic, f"Mensaje {i}", qos=1)
    print(f"Publicado Mensaje {i}")
    time.sleep(0.1)  # Muy rápido

client.loop_stop()
client.disconnect()
