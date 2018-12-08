
from pyfronius import fronius
from fronius2mqtt import device

class Flow(device.Device):

	def __init__(self, config):
		self.host = config['host']
		self.topic = config['topic']
		self.fronius = fronius.Fronius(self.host)

	def update(self):
		data = self.fronius.current_power_flow()
		return data
