import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import json

broker = "broker.emqx.io"
topic = "uma/mqtt5/payload_format"

# Crear cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
client.connect(broker, 1883)

# Propiedades: indicamos que el payload es texto UTF-8
props = Properties(PacketTypes.PUBLISH)
props.PayloadFormatIndicator = 1  # 1 = texto, 0 binario

# Publicamos un texto
payload = "Hola desde MQTT con formato texto"
client.publish(topic, payload=payload, qos=1, properties=props)

# Publicamos un JSON
payload = {
    "sensor": "temp",
    "value": 23.5
}

props = Properties(PacketTypes.PUBLISH)
props.PayloadFormatIndicator = 1  # texto
props.ContentType = "application/json"

client.publish(topic, json.dumps(payload), qos=1, properties=props)

client.disconnect()
