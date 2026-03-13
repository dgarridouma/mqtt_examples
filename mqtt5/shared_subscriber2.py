import paho.mqtt.client as mqtt
from time import sleep

def on_message(client, userdata, msg):
    print(f"{userdata} recibió: {msg.payload.decode()}")

broker = "broker.emqx.io"
#broker = "localhost"

# Cliente 2 (worker2)
client2 = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata="Worker 2", protocol=mqtt.MQTTv5)
client2.on_message = on_message
client2.connect(broker, 1883)
client2.subscribe("$share/grupo1/uma/mqtt5/shared")

client2.loop_start()
while True:
    sleep(1)
