# import re
# asa_conn =asa_conn = "TCP Student 192.168.189.167:32806 Teacher 157.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n " \
#                      "TCP Student 192.168.189.167:80 Teacher 157.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
#
# asa_dict={}
#
# for conn in asa_conn.split('\n'):
#     re_result=re.match()
#     asa_dict[]=()
#
# print('打印分析后的字典！\n')
# print(asa_dict)
#
#
# src='src'
# src_ip='src_ip'
# dst='dst'
# dst_ip='dst_ip'
# bytes_name='bytes'
# flags='flags'
# fromat_str1=
# fromat_str2=
#
# print('\n格式化打印输出\n')
#
# for key,value in asa_dict.items():
#

import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 157.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 157.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}

pattern = re.compile(
    r'TCP Student (\d+\.\d+\.\d+\.\d+):(\d+) '
    r'Teacher (\d+\.\d+\.\d+\.\d+):(\d+), '
    r'idle \S+, bytes (\d+), flags (\S+)'
)

for conn in asa_conn.split('\n'):
    conn = conn.strip()
    if not conn:
        continue
    re_result = pattern.match(conn)
    if re_result:
        key = (re_result.group(1), re_result.group(2), re_result.group(3), re_result.group(4))
        value = (re_result.group(5), re_result.group(6))
        asa_dict[key] = value

print('打印分析后的字典！\n')
print(asa_dict)

src = 'src'
src_port = 'src_port'
dst = 'dst'
dst_port = 'dst_port'
bytes_name = 'bytes'
flags = 'flags'

format_str1 = "{src:^15}: {0:^15} | {src_port:^15}: {1:^15} | {dst:^15}: {2:^15} | {dst_port:^15}: {3:^15}"
format_str2 = "{bytes:^15}: {0:^15} | {flags:^15}: {1:^15}"

print('\n格式化打印输出\n')
for key, value in asa_dict.items():
    src_ip_val, src_port_val, dst_ip_val, dst_port_val = key
    bytes_val, flags_val = value

    print(format_str1.format(
        src_ip_val, src_port_val, dst_ip_val, dst_port_val,
        src=src, src_port=src_port, dst=dst, dst_port=dst_port
    ))
    print(format_str2.format(
        bytes_val, flags_val,
        bytes=bytes_name, flags=flags
    ))
    print("=" * 140)

port_list = [
    'eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7',
    'eth 1/101/2/46', 'eth 1/101/1/34', 'eth 1/101/1/18', 'eth 1/101/1/13',
    'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8'
]


sorted_port_list = sorted(port_list, key=lambda x: tuple(map(int, x.split('/')[2:])))

print("排序后的端口列表：")
print(sorted_port_list)
