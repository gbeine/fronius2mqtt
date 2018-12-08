
import logging
import paho.mqtt.client as mqtt

class Mqtt:

	def __init__(self, config):
		self.config = config

	def connect(self):
		self.client = mqtt.Client()
		self.client.username_pw_set(self.config['user'], self.config['password'])
		self.client.connect(self.config['host'], self.config['port'])
		self.client.loop_start()

	def disconnect(self):
		self.client.disconnect()

	def publish(self, topic, payload):
		topic = "{}/{}".format(self.config['topic'], topic)
		logging.info("Publish %s: %s", topic, payload)
		self.client.publish(topic, payload)
