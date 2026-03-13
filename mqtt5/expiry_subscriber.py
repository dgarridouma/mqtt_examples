import time
import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

broker = "broker.emqx.io"
port = 1883
topic = "uma/mqtt5/session_expiry"


def on_connect(client, userdata, flags, rc, properties):
    print(f"[on_connect] Conectado con código: {rc}")
    print(f"[on_connect] ¿Sesión reanudada?: {flags.session_present}")
    client.subscribe(topic, qos=1)
    print("[Subscriber] Suscrito. Esperando mensajes...")



# Callback cuando el cliente recibe un mensaje
def on_message(client, userdata, msg):
    print(f"[{time.ctime()}] Mensaje recibido en '{msg.topic}': {msg.payload.decode()}")

# -------------------------------
# Cliente SUSCRIPTOR con Session Expiry
# -------------------------------
def subscriber():
    # Propiedades para CONNECT con expiración de sesión (30 segundos)
    connect_props = Properties(PacketTypes.CONNECT)
    connect_props.SessionExpiryInterval = 30  # segundos

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="sub_clientdgm", protocol=mqtt.MQTTv5)
    client.on_connect = on_connect
    client.on_message = on_message

    # Conectarse sin clean start (reutiliza sesión previa si existe)
    client.connect(broker, port, keepalive=60, clean_start=False, properties=connect_props)
    client.loop_forever()


if __name__ == "__main__":
    subscriber()       # Inicia el suscriptor
