# # # import re
# # #
# # # str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
# # # vlanid_pattern = r'^(\d+)'
# # # mac_pattern = r'\b([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})\b'  # 使用捕获组
# # # type_pattern = r'\b([A-Z]+)\b(?=\s+[A-Za-z0-9/]+$)'  # 修改为确保类型字段后面紧跟接口名称并位于字符串末尾
# # # interface_pattern = r'([A-Za-z]+/\d+/\d+)$'  # 去掉 \b 并确保位于字符串末尾
# # #
# # # # 搜索匹配
# # # vlan_id = re.search(vlanid_pattern, str1).group(1)
# # # mac_address = re.search(mac_pattern, str1).group(1)
# # # type_ = re.search(type_pattern, str1).group(1)  # 使用 group(1)
# # # interface = re.search(interface_pattern, str1).group(1)  # 使用 group(1)
# # # print('VLAN ID{:>10}:{}'.format(' ', vlan_id))
# # # print('MAC{:>10}:{}'.format(' ', mac_address))
# # # print('Type{:>10}:{}'.format(' ', type))
# # # print('Interface{:>10}:{}'.format(' ', interface))
# # import re
# #
# # str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
# #
# # # 定义各部分的正则表达式模式
# # vlanid_pattern = r'^(\d+)'
# # mac_pattern = r'\b([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})\b'  # 使用捕获组
# # type_pattern = r'\b([A-Z]+)\b(?=\s+[A-Za-z0-9/]+\s*$)'  # 修改为确保类型字段后面紧跟接口名称并位于字符串末尾
# # interface_pattern = r'\s*([A-Za-z]+/\d+/\d+)\s*$'  # 允许接口名称前有任意数量的空白字符，并确保位于字符串末尾
# #
# # # 搜索匹配
# # vlan_id = re.search(vlanid_pattern, str1).group(1)
# # mac_address = re.search(mac_pattern, str1).group(1)
# # type_ = re.search(type_pattern, str1).group(1)  # 使用 group(1)
# # interface = re.search(interface_pattern, str1).group(1)  # 使用 group(1)
# #
# # # 格式化输出
# # print('VLAN ID{:>10}: {}'.format(' ', vlan_id))
# # print('MAC{:>10}: {}'.format(' ', mac_address))
# # print('Type{:>10}: {}'.format(' ', type_))
# # print('Interface{:>10}: {}'.format(' ', interface))
#
# import re
#
# str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
#
# # 定义各部分的正则表达式模式
# vlanid_pattern = r'^(\d+)'
# mac_pattern = r'\b([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})\b'  # 使用捕获组
# type_pattern = r'\b([A-Z]+)\b(?=\s+[A-Za-z0-9/]+\s*$)'  # 修改为确保类型字段后面紧跟接口名称并位于字符串末尾
# interface_pattern = r'\s*([A-Za-z]+/\d+/\d+)\s*$'  # 允许接口名称前有任意数量的空白字符，并确保位于字符串末尾
#
# # 搜索匹配
# vlan_id_match = re.search(vlanid_pattern, str1)
# mac_address_match = re.search(mac_pattern, str1)
# type_match = re.search(type_pattern, str1)
# interface_match = re.search(interface_pattern, str1)
#
# # 检查匹配结果并提取内容
# if vlan_id_match:
#     vlan_id = vlan_id_match.group(1)
# else:
#     vlan_id = 'N/A'
#
# if mac_address_match:
#     mac_address = mac_address_match.group(1)
# else:
#     mac_address = 'N/A'
#
# if type_match:
#     type_ = type_match.group(1)
# else:
#     type_ = 'N/A'
#
# if interface_match:
#     interface = interface_match.group(1)
# else:
#     interface = 'N/A'
#
# # 格式化输出
# print('VLAN ID{:>10}: {}'.format(' ', vlan_id))
# print('MAC{:>10}: {}'.format(' ', mac_address))
# print('Type{:>10}: {}'.format(' ', type_))
# print('Interface{:>10}: {}'.format(' ', interface))

import re


str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'


str1 = str1.strip()


vlanid_pattern = r'^(\d+)'
mac_pattern = r'\b([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})\b'
type_pattern = r'\b([A-Z]+)\b'
interface_pattern = r'\b([A-Za-z]+\d+/\d+/\d+)\b'

vlan_id_match = re.search(vlanid_pattern, str1)
mac_address_match = re.search(mac_pattern, str1)
type_match = re.search(type_pattern, str1)
interface_match = re.search(interface_pattern, str1)

vlan_id = vlan_id_match.group(1)
mac_address = mac_address_match.group(1)
type = type_match.group(1)
interface = interface_match.group(1)

field_width = 15
print('{:<{width}}: {}'.format('VLAN ID', vlan_id, width=field_width))
print('{:<{width}}: {}'.format('MAC', mac_address, width=field_width))
print('{:<{width}}: {}'.format('Type', type, width=field_width))
print('{:<{width}}: {}'.format('Interface', interface, width=field_width))

import re

str2 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

protocolr_pattern = r'(?P<protocol>\w+)\s+'
server_ip_pattern = r'server\s+(?P<server_ip>\d+\.\d+\.\d+\.\d+:\d+)\s+'
local_ip_pattern = r'localserver\s+(?P<local_ip>\d+\.\d+\.\d+\.\d+:\d+),\s+'
idle_time_pattern = r'idle\s+(?P<idle_time>\d+:\d+:\d+),\s+'
bytes_pattern = r'bytes\s+(?P<bytes>\d+),\s+'
flags_pattern = r'flags\s+(?P<flags>\w+)'

protocol_match = re.search(protocolr_pattern, str2)
server_ip_match = re.search(server_ip_pattern, str2)
local_ip_match = re.search(local_ip_pattern, str2)
idle_time_match = re.search(idle_time_pattern, str2)
bytes_match = re.search(bytes_pattern, str2)
flags_match = re.search(flags_pattern, str2)

protocol = protocol_match.group('protocol')
server_ip = server_ip_match.group('server_ip')
local_ip = local_ip_match.group('local_ip')
idle_time = idle_time_match.group('idle_time')
bytes_ = bytes_match.group('bytes')
flags = flags_match.group('flags')

field_width = 15
print(f"{'protocol':<{field_width}}: {protocol}")
print(f"{'server':<{field_width}}: {server_ip}")
print(f"{'localserver':<{field_width}}: {local_ip}")
print(f"{'idle':<{field_width}}: {idle_time.replace(':', ' 小时 ').replace(':', '分钟 ') + '秒'}")
print(f"{'bytes':<{field_width}}: {bytes_}")
print(f"{'flags':<{field_width}}: {flags}")
