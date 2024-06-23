# fronius2mqtt

A Fronius HTTP API to MQTT bridge

Attention: This is a complete rewrite of the bridge.
While the old fronius2mqtt brigde used polling the inverters to fetch the  data, the new version make use of the push feature provided by Fronius Symo.

The daemon offers no HTTP endpoints which can be configured in the configuration interface of each inverter.
It forwards the data directly to MQTT.

## Install

### Installation using Docker

docker run -it --rm --name fronius2mqtt -v fronius2mqtt.conf:/etc/fronius2mqtt.conf docker.io/gbeine/fronius2mqtt

### Native installation with Python venv

- clone the git repository
- ensure to have Python 3 with venv installed
- run the ```install``` script in the local directory

## Configuration

Each configuration option is also available as command line argument.

- copy ```fronius2mqtt.conf.example```
- configure as you like

| option           | default                  | arguments           | comment                                                                                |
|------------------|--------------------------|---------------------|----------------------------------------------------------------------------------------|
| mqtt_host        | 'localhost'              | -m, --mqtt_host     | The hostname of the MQTT server.                                                       |
| mqtt_port        | 1883                     | --mqtt_port         | The port of the MQTT server.                                                           |
| mqtt_keepalive   | 30                       | --mqtt_keepalive    | The keep alive interval for the MQTT server connection in seconds.                     |
| mqtt_clientid    | 'fronius2mqtt'           | --mqtt_clientid     | The clientid to send to the MQTT server.                                               |
| mqtt_user        | -                        | -u, --mqtt_user     | The username for the MQTT server connection.                                           |
| mqtt_password    | -                        | -p, --mqtt_password | The password for the MQTT server connection.                                           |
| mqtt_topic       | 'fronius'                | -t, --mqtt_topic    | The topic to publish MQTT message.                                                     |
| mqtt_tls_version | 'TLSv1.2'                | --mqtt_tls_version  | The TLS version to use for MQTT. One of TLSv1, TLSv1.1, TLSv1.2.                       |
| mqtt_verify_mode | 'CERT_REQUIRED'          | --mqtt_verify_mode  | The SSL certificate verification mode. One of CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED. |
| http_host        | 'localhost'              | --http_host         | The address of the HTTP server.                                                        |
| http_port        | 8080                     | --http_port         | The port of the HTTP server.                                                           |
| verbose          | -                        | -v, --verbose       | Be verbose while running.                                                              |
| -                | '/etc/fronius2mqtt.conf' | -c, --config        | The path to the config file.                                                           |
