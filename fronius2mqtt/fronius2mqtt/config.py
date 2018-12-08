import yaml
import logging
import logging.config

class Config:
	"""Class for parsing fronius2mqtt.yaml."""
	
	def __init__(self):
		"""Initialize Config class."""
		logging.config.fileConfig('logging.conf')
		self._mqtt = {}
		self._fronius = {}
	
	
	def read(self, file='fronius2mqtt.yaml'):
		"""Read config."""
		logging.debug("Reading %s", file)
		try:
			with open(file, 'r') as filehandle:
				config = yaml.load(filehandle)
				self._parse_mqtt(config)
				self._parse_fronius(config)
		except FileNotFoundError as ex:
			logging.error("Error while reading %s: %s", file, ex)

	def _parse_mqtt(self, config):
		"""Parse the mqtt section of fronius2mqtt.yaml."""
		if "mqtt" in config:
			self._mqtt = config["mqtt"]
		if not "host" in self._mqtt:
				raise ValueError("MQTT host not set")
		if not "port" in self._mqtt:
				raise ValueError("MQTT port not set")
		if not "user" in self._mqtt:
				raise ValueError("MQTT user not set")
		if not "password" in self._mqtt:
				raise ValueError("MQTT password not set")
		if not "topic" in self._mqtt:
				raise ValueError("MQTT topic not set")
				

	def _parse_fronius(self, config):
		"""Parse the fronius section of fronius2mqtt.yaml."""
		if "fronius" in config:
			self._fronius = config["fronius"]
		for item in  self._fronius:
			if len(item) != 1:
				raise ValueError("Fronius device configuration contains more than one item.")
			for (type, properties) in item.items():
				if not "host" in properties:
					raise ValueError("Missing host for Fronius device")
				if not "topic" in properties:
					raise ValueError("Missing topic for Fronius device")

	def mqtt(self):
		return self._mqtt

	def fronius(self):
		return self._fronius
