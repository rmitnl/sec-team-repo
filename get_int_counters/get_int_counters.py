import sys
from vars import *
from netmiko import ConnectHandler

# check for 2 args
if len(sys.argv) != 3:
    print('2 args required')
    sys.exit(1)

if argv[1][0:7] != "--device":
    print('No device ip')
    sys.exit(1)

if argv[2][0:11] != "--interface":
    print('No interface name')
    sys.exit(1)

print(sys.argv[1:])
device_ip=sys.argv[1]
inter_name=sys.argv[2]

#device = ConnectHandler(device_type='brocade_fastiron', ip=device_ip, username=var_u, password=var_p,secret=var_s)
#output = device.send_command("show statistics "+inter_name)
#print (output)

#device.disconnect()


args = []
out='{"args":['
for i in sys.argv[1:]:
    if i[0:5] != "--arg":
        out += '"' + i + "\","
        args.append(i)
out = out[:-1] + "]}"
print(out)
