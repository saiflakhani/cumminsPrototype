# Cummins Prototype
A project to calculate bus checkin times using BLE Mesh

## Backend
A python backend that checks MQTT for messages, and has an RSSI threshold that can be changed to calculate whether a tag has entered the premises

## Frontend
HTML CSS Bootstrap frontend that calls the Flask APIs

## Data Model
```{"time":1611834728,"data":{"type":"01","node":"0x0003","rssi":"-52","mac":"8b2b"}}```
