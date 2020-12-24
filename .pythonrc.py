import logging, sonos.subnet, rlcompleter
from sonos.services.common import wait_until_true

modules = [
        'SONOS.telnet_client',
        'SONOS.sonos.services',
        'SONOS.sonos.upnp',
        'SONOS.UDPLogger',
        'SONOS.sonos.client',
        'SONOS.sonos.upnp',
        'SONOS.coherence.upnp',
        'urllib3.connectionpool',
        'SONOS.sonos.services.base',
        'SONOS.Coherence.upnp.core.service'
    ]
for module in modules:
    logging.getLogger(module).setLevel(logging.INFO)
net = sonos.subnet.Devices()
zones = net.allDevices
#wait_until_true(lambda: len(zones) > 0 and len(net.get_devices_with_built_in_speakers()) > 0, iteration_delay=1)
#zp = [zp for zp in net.allDevices if hasattr(zp, 'ContentDirectory')][0]
zp = [zp for zp in net.allDevices if zp.serialNumber == '7828CA1004FA'][0]
wait_until_true(lambda: len(zones) >= 1, iteration_delay=1)
for z in zones: vars()[z.modelNumber.lower()] = z
rlcompleter.readline.parse_and_bind("tab:complete")
