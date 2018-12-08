
from fronius2mqtt import inverter
from fronius2mqtt import storage
from fronius2mqtt import flow
from fronius2mqtt import meter

class FroniusFactory:

	def __init__(self, config):
		self.config = config

	def create_devices(self):
		devices = []
		for c in self.config:
			(type, properties) = c.popitem()
			if not type in factory:
				raise ValueError("Not a valid device: {}".format(type))
			device = factory[type](properties)
			devices.append(device)
		return devices
	
def _create_inverter(properties):
	device = inverter.Inverter(properties)
	return device

def _create_storage(properties):
	device = storage.Storage(properties)
	return device

def _create_meter(properties):
	device = meter.Meter(properties)
	return device

def _create_flow(properties):
	device = flow.Flow(properties)
	return device

factory = {
	"inverter" : _create_inverter,
	"storage" : _create_storage,
	"meter" : _create_meter,
	"flow" : _create_flow
}
