
import logging

class Device:

	def update(self):
		raise NotImplementedError("update not implemented")

	def update_and_publish(self, mqtt):
		data = self.update()
		for (key, value) in data.items():
			if 'value' in value:
				mqtt.publish("{}/{}".format(self.topic, key), value['value'])
			else:
				logging.info("Ignore %s: %s", key, value)
			