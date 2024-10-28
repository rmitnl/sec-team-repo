import sys
from vars import *
from netmiko import ConnectHandler

print(sys.argv[1:])
# check for 2 args
if len(sys.argv) != 3:
    print('2 args required')
    sys.exit(1)

device = sys.argv[1]
interface = sys.argv[2]

#check for correct args
if device[0:8] != "--device":
    print('No device ip')
    sys.exit(1)

if interface[0:11] != "--interface":
    print('No interface name')
    sys.exit(1)

# extract variables
device = device[9:]
interface = interface[12:]

print (device,interface)
network = ConnectHandler(device_type='brocade_fastiron', ip=device, username=var_u, password=var_p,secret=var_s)
output = network.send_command("show statistics "+interface)
print (output)

network.disconnect()
