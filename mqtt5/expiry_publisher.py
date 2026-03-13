import time
import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

broker = "broker.emqx.io"
port = 1883
topic = "uma/mqtt5/session_expiry"


# -------------------------------
# Cliente PUBLICADOR con Message Expiry
# Lanzarlo después de que el suscriptor se desconecte por primera vez
# Si lanzamos al suscriptor otra vez después de 5 segundos el mensaje se pierde aunque
# se mantenga la sesión
# -------------------------------
def publisher():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="pub_clientdgm", protocol=mqtt.MQTTv5)
    client.connect(broker, port)

    # Propiedad de expiración del mensaje (5 segundos)
    props = Properties(PacketTypes.PUBLISH)
    props.MessageExpiryInterval = 5  # en segundos

    client.publish(topic, payload="Hola con expiración!", qos=1, properties=props)
    print("[Publisher] Mensaje enviado con expiración de 5s")
    client.disconnect()

if __name__ == "__main__":
    publisher()
    