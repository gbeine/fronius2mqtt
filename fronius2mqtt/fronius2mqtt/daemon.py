
import time

from fronius2mqtt import froniusfactory
from fronius2mqtt import mqtt

class Daemon:

	def __init__(self, config):
		self.config = config
		self.devices = []
		self._init_mqtt()
		self._init_fronius()

	def run(self):
		while True:
			for device in self.devices:
				device.update_and_publish(self.mqtt)
			time.sleep(5)

	def _init_mqtt(self):
		self.mqtt = mqtt.Mqtt(self.config.mqtt())
		self.mqtt.connect()

	def _init_fronius(self):
		factory = froniusfactory.FroniusFactory(self.config.fronius())
		self.devices = factory.create_devices()
