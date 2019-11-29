# simple inquiry example
from bluetooth import *

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))

# # Run on brickpi
# import os
# hostname = "192.168.0.100"
# response = os.system("ping -c 1 " + hostname)

# #and then check the response...
# if response == 0:
#   print(hostname, 'is up!')
# else:
#   print(hostname, 'is down!')

# #Green Bot - 192.168.0.104
# #Blue Bot - 192.168.0.100
# #To find ip address: write in terminal 'ifconfig' in the output look for 'inet' under 'wlan0' and the ip