# fronius2mqtt - A Fronius HTTP API to MQTT bridge

Attention: This is a complete rewrite of the bridge.
While the old fronius2mqtt brigde used polling the inverters to fetch the  data, the new version make use of the push feature provided by Fronius Symo.

The daemon offers now HTTP endpoints which can be configured in the configuration interface of each inverter.
It forwards the data directly to MQTT.

## Install

### Installation using Docker

```
docker run -it --rm --name fronius2mqtt -v fronius2mqtt.conf:/etc/fronius2mqtt.conf docker.io/gbeine/fronius2mqtt
```

### Native installation with Python venv

- clone the git repository
- ensure to have Python 3 with venv installed
- run the `install` script in the local directory

## Configuration

### Device configuration

On the settings page for you Fronius device, select 'Push Service'.

Define an identifier for your device, e.g. `fronius1`, and add the following values:

| Field            | Explanation                                                                  |
|------------------|------------------------------------------------------------------------------|
| Name             | As you like, only relevant on the device side                                |
| Data Format      | Select one from the table below, choose HTTP Post                            |
| Interval         | 10 sec, or use the default                                                   |
| Activate         | Select                                                                       |
| Server:Port      | The hostname and port of your HTTP server, e.g. `smarthome.example.org:8080` |
| Upload file name | /path/identifier, e.g. `/current_data_inverter/fronius1`                     |
| Login            | Not needed unless you use an authentication proxy                            |
| Proxy            | Not needed unless you use a dedicated proxy server                           |

| Data format                                     | URL path                                          |
|-------------------------------------------------|---------------------------------------------------|
| Datamanager IO States                           | `/datamanager_io_states/<device identifier>`      |
| SolarAPI v1 - CurrentData - Inverter            | `/current_data_inverter/<device identifier>`      |
| SolarAPI v1 - CurrentData - Meter               | `/current_data_meter/<device identifier>`         |
| SolarAPI v1 - CurrentData - Powerflow           | `/current_data_powerflow/<device identifier>`     |
| SolarAPI v1 - CurrentData - SensorCard          | `/current_data_sensorcard/<device identifier>`    |
| SolarAPI v1 - CurrentData - StringControl       | `/current_data_stringcontrol/<device identifier>` |
| SolarAPI v1 - Logdata - Data                    | `/logdata_data/<device identifier>`               |
| SolarAPI v1 - Logdata - Errors and Events       | `/logdata_errors_and_events/<device identifier>`  |
| SunSpec Datalogger v1.0b - inverter float model | - not yet implemented -                           |
| SunSpec Datalogger v1.2 - meter model           | - not yet implemented -                           |

### fronius2mqtt.conf

Each configuration option is also available as command line argument.

- copy ```fronius2mqtt.conf.example```
- configure as you like

| option               | default                  | arguments               | comment                                                                                |
|----------------------|--------------------------|-------------------------|----------------------------------------------------------------------------------------|
| `mqtt_host`          | 'localhost'              | `-m`, `--mqtt_host`     | The hostname of the MQTT server.                                                       |
| `mqtt_port`          | 1883                     | `--mqtt_port`           | The port of the MQTT server.                                                           |
| `mqtt_keepalive`     | 30                       | `--mqtt_keepalive`      | The keep alive interval for the MQTT server connection in seconds.                     |
| `mqtt_clientid`      | 'fronius2mqtt'           | `--mqtt_clientid`       | The clientid to send to the MQTT server.                                               |
| `mqtt_user`          | -                        | `-u`, `--mqtt_user`     | The username for the MQTT server connection.                                           |
| `mqtt_password`      | -                        | `-p`, `--mqtt_password` | The password for the MQTT server connection.                                           |
| `mqtt_topic`         | 'fronius'                | `-t`, `--mqtt_topic`    | The topic to publish MQTT message.                                                     |
| `mqtt_tls`           | -                        | `--mqtt_tls`            | Use SSL/TLS encryption for MQTT connection.                                            |
| `mqtt_tls_version`   | 'TLSv1.2'                | `--mqtt_tls_version`    | The TLS version to use for MQTT. One of TLSv1, TLSv1.1, TLSv1.2.                       |
| `mqtt_verify_mode`   | 'CERT_REQUIRED'          | `--mqtt_verify_mode`    | The SSL certificate verification mode. One of CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED. |
| `mqtt_ssl_ca_path`   | -                        | `--mqtt_ssl_ca_path`    | The SSL certificate authority file to verify the MQTT server.                          |
| `mqtt_tls_no_verify` | -                        | `--mqtt_tls_no_verify`  | Do not verify SSL/TLS constraints like hostname.                                       |
| `http_host`          | 'localhost'              | `--http_host`           | The address of the HTTP server.                                                        |
| `http_port`          | 8080                     | ``--http_port``         | The port of the HTTP server.                                                           |
| `timestamp`          | -                        | `-z`, `--timestamp`     | Publish timestamps for all topics, e.g. for monitoring purposes.                       |
| `verbose`            | -                        | `-v`, `--verbose`       | Be verbose while running.                                                              |
| -                    | '/etc/fronius2mqtt.conf' | `-c`, `--config`        | The path to the config file.                                                           |


## Disclaimer

''Attention:'' Please be aware that the data is published over plain HTTP by this solution.
Use with care ond only if you know what you're doing.

## Future plans

- Support for HTTPS
- Authentication support
- Support for new Fronius API

## Running fronius2mqtt

I use [systemd](https://systemd.io/) to manage my local services.

## Support

I have not the time (yet) to provide professional support for this project.
But feel free to submit issues and PRs, I'll check for it and honor your contributions.

## License

The whole project is licensed under BSD-3-Clause license. Stay fair.
