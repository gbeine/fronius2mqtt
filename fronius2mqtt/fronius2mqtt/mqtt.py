
import logging
import paho.mqtt.client as mqtt

class Mqtt:

	def __init__(self, config):
		self._config = config

	def connect(self):
		self._client = mqtt.Client()
		self._client.username_pw_set(self._config['user'], self._config['password'])
		self._client.connect(self._config['host'], self._config['port'])
		self._client.loop_start()

	def disconnect(self):
		self.client.disconnect()

	def publish(self, topic, payload):
		topic = "{}/{}".format(self._config['topic'], topic)
		logging.info("Publish %s: %s, %s, %s", topic, payload, self._config["qos"], self._config["retain"])
		self._client.publish(topic, payload, self._config["qos"], self._config["retain"])
