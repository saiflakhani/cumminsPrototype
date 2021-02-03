import mqtt_messaging

def set_limit(rssi):
    mqtt_messaging.RSSI_LIMIT_TO_ENTRY = rssi
    return {"rssi": mqtt_messaging.RSSI_LIMIT_TO_ENTRY}

def read_limit():
    return {"rssi": mqtt_messaging.RSSI_LIMIT_TO_ENTRY}