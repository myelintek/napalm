

from napalm import get_network_driver

driver = get_network_driver('nvidia_cumulus')
device = driver('100.74.5.232', 'cumulus', 'Giga@89124000')
device.open()
print("facts: {}".format(device.get_facts()))
device.close()
