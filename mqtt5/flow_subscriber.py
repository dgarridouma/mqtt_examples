import threading
import time
import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import logging
import sys

# Configura el logger global para mostrar DEBUG en consola
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)


broker = "broker.emqx.io"
topic = "uma/mqtt5/flowcontrol"

def on_connect(client, userdata, flags, rc, properties=None):
    print("Conectado al broker. Suscribiéndose...")
    client.subscribe(topic, qos=1)

def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()}")
    time.sleep(3)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)

conn_props = Properties(PacketTypes.CONNECT)
conn_props.ReceiveMaximum = 3
# No se observa visualmente ningún comportamiento con respecto a ReceiveMaximum

client.on_connect = on_connect
client.on_message = on_message

client.enable_logger()
client.connect(broker, 1883, properties=conn_props)
client.loop_forever()
