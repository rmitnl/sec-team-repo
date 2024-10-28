import sys
from vars import *
from netmiko import ConnectHandler

# check for 2 args
if len(sys.argv) != 3:
    print('2 args required')
    sys.exit(1)

#check for correct args
device = sys.argv[1]
if device[0:8] != "--device":
    print('No device ip')
    sys.exit(1)

interface = sys.argv[2]
if interface[0:11] != "--interface":
    print('No interface name')
    sys.exit(1)

# extract data from args 
device = device[9:]
device = device.strip('\"')
interface = interface[12:]
interface = interface.strip('\"')

# run the show command
#print (device,interface)
network = ConnectHandler(device_type='brocade_fastiron', ip=device, username=var_u, password=var_p,secret=var_s)
output = network.send_command("show statistics "+interface)

# show output
print (output)
network.disconnect()
