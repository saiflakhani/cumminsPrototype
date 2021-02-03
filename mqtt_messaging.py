import paho.mqtt.client as mqtt
import config
import simplejson as json
import utils
import db

client = None
conn = None
cursor = None
RSSI_LIMIT_TO_ENTRY = -70

def on_connect(client, userdata, flags, rc):
    global conn, cursor
    print("Connected with result code "+str(rc))
    cursor, conn = db.connection()
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(config.MQTT_SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    cursor, conn = db.connection()
    try:
        trigger_obj = json.loads(msg.payload)
        if trigger_obj is not None and 'data' in trigger_obj.keys():
            if 'node' in trigger_obj['data'].keys() and 'rssi' in trigger_obj['data'].keys():
                if int(trigger_obj['data']['rssi']) > RSSI_LIMIT_TO_ENTRY:
                    query = "INSERT INTO bus_checkins(lpn_id, mac_addr, rssi) VALUES ('{0}', '{1}', {2});".format(trigger_obj['data']['node'], trigger_obj['data']['mac'], int(trigger_obj['data']['rssi']))
                    print(query)
                    cursor.execute(query)
                    conn.commit()
                    conn.close()

    except Exception as e:
        print("Error in on_message: "+str(e))
        if conn is not None:
            conn.close()


def init_mqtt():
    global client
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.tls_set_context(context=None)
        client.tls_insecure_set(True)
        client.username_pw_set(username= config.MQTT_USERNAME, password=config.MQTT_PASSWORD)
        client.connect(config.MQTT_BROKER, config.MQTT_PORT, 60)
        client.loop_start()
    except Exception as e:
        print("There was an error initializing MQTT: "+ str(e))