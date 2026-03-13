import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Conectado con código de resultado:", rc)
    properties = mqtt.Properties(mqtt.PacketTypes.PUBLISH)
    properties.UserProperty = ("key2", "value2")

    client.publish("uma/mqtt5/properties", "Mensaje con propiedades2", properties=properties, qos=1, retain=False)
    print("Publicado mensaje con propiedades")

broker = "broker.emqx.io"
# broker = "localhost"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)  # Versión 2 para MQTT 5

client.on_connect = on_connect
client.connect(broker, 1883)

properties = mqtt.Properties(mqtt.PacketTypes.PUBLISH)
properties.UserProperty = ("key1", "value1")

client.publish("uma/mqtt5/properties", "Mensaje con propiedades", properties=properties, qos=1, retain=False)
client.loop_forever()
