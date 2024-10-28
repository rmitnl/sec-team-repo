import sys
from vars import *
from netmiko import ConnectHandler

# check for 2 args
if len(sys.argv) != 3:
    print('2 args required')
    sys.exit(1)

print(sys.argv[1:])
device_ip=sys.argv[1]
inter_name=sys.argv[2]

device = ConnectHandler(device_type='brocade_fastiron', ip=device_ip, username=var_u, password=var_p,secret=var_s)
output = device.send_command("show statistics "+inter_name)
print (output)

device.disconnect()
