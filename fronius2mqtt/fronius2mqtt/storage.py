
from pyfronius import fronius
from fronius2mqtt import device

class Storage(device.Device):

	def __init__(self, config):
		self.host = config['host']
		if 'device' in config:
			self.device = config['device']
		else:
			self.device = 0
		self.topic = config['topic']
		self.fronius = fronius.Fronius(self.host)

	def update(self):
		data = self.fronius.current_storage_data(self.device)
		return data
