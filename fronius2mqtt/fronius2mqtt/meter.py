
from pyfronius import fronius
from fronius2mqtt import device

class Meter(device.Device):

	def __init__(self, config):
		self.host = config['host']
		if 'device' in config:
			self.device = config['device']
		self.topic = config['topic']
		self.fronius = fronius.Fronius(self.host)

	def update(self):
		if hasattr(self, 'device'):
			data = self.fronius.current_meter_data(self.device)
		else:
			data = self.fronius.current_system_meter_data()
		return data
