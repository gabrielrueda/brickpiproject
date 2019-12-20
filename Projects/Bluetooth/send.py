import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))
for addr, name, port in nearby_devices:
    print("  {} - {} - {}".format(addr, name, port))

# serverMACAddress = 'B8:27:EB:55:C0:33'
# port = 3
# s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# s.connect((serverMACAddress, port))
# while 1:
#     text = raw_input() # Note change to the old (Python 2) raw_input
#     if text == "quit":
#         break
#     s.send(text)
# s.close()
