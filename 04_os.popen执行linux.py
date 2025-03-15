import os
import re

ifconfig_result = os.popen('ifconfig ens160').read()

ipv4_add = re.findall(r'inet (\d+\.\d+\.\d+\.\d+)', ifconfig_result)
netmask = re.findall(r'netmask (\d+\.\d+\.\d+\.\d+)', ifconfig_result)
broadcast = re.findall(r'broadcast (\d+\.\d+\.\d+\.\d+)', ifconfig_result)
mac_addr = re.findall(r'ether ([0-9a-fA-F:]{17})', ifconfig_result)
# ipv4_add = re.findall()
# netmask = re.findall()
# broadcast = re.findall()
# mac_addr = re.findall()

format_string = '{:<15}: {}'

print(format_string.format('IPv4 Address', ipv4_add[0]))
print(format_string.format('Netmask', netmask[0]))
print(format_string.format('Broadcast', broadcast[0]))
print(format_string.format('MAC Address', mac_addr[0]))

ipv4_gw = '192.168.124.254'
print('\n我们假设网关IP地址为最后一位254，因此此网关IP地址为:' + ipv4_gw + '\n')
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()
re_ping_result = re.search(r'1 received|1 packets received', ping_result)

if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')
