import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import time

broker = "broker.emqx.io"
topic = "uma/mqtt5/topic/alias/demo"
topic_alias = 10  # Puedes usar cualquier número > 0, mientras el broker lo acepte

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)  # Versión 2 para MQTT 5
client.connect(broker, 1883)
client.loop_start()

# Primer mensaje: se establece el alias
props1 = Properties(PacketTypes.PUBLISH)
props1.TopicAlias = topic_alias
client.publish(topic, payload="Mensaje con alias definido", qos=1, properties=props1)
print("Enviado: mensaje con topic y alias")

time.sleep(1)

# Segundo mensaje: solo se envía el alias, sin topic
props2 = Properties(PacketTypes.PUBLISH)
props2.TopicAlias = 10
client.publish(topic='', payload="Mensaje usando solo el alias", qos=1, properties=props2)
print("Enviado: mensaje con alias inexistente")

time.sleep(1)
client.loop_stop()
client.disconnect()
