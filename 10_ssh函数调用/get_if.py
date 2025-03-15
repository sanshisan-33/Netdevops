from ssh_paramiko import qytang_ssh
from monitor_http import qytang_ping
import re
import pprint


def qytang_get_if(*ips, username='admin', password='Cisco123'):
    device_if_dict = {}

    for ip in ips:
        ping_result = qytang_ping(ip)
        if not ping_result:
            print(f" {ip} 不可达")
            continue

        result = qytang_ssh(ip, username=username, password=password, cmd='show ip int brief')

        lines = result.strip().split('\n')[1:]
        interfaces = {}
        for line in lines:
            parts = line.split()
            if len(parts) >= 2 and re.match(r'\d+\.\d+\.\d+\.\d+', parts[1]):
                interface = parts[0]
                ipaddress = parts[1]
                interfaces[interface] = ipaddress

        device_if_dict[ip] = interfaces
    return device_if_dict


if __name__ == '__main__':
    pprint.pprint(qytang_get_if('10.10.1.1', '10.10.1.10', username='admin', password='Cisco123'), indent=4)

#
# def qytang_get_if(*ips, username='admin', password='Cisco123'):
#     device_if_dict = {}
#     for ip in ips:
#         try:
#             # 使用SSH连接到设备并执行命令
#             output = qytang_ssh(ip, username, password, cmd='show ip interface brief')
#
#             # 解析命令输出
#             interfaces = {}
#             lines = output.split('\n')
#             for line in lines:
#                 # 根据实际输出格式调整正则表达式
#                 match = re.search(r'(\S+)\s+([\d\.]+)', line)
#                 if match:
#                     interface_name = match.group(1)
#                     ip_address = match.group(2)
#                     interfaces[interface_name] = ip_address
#
#             device_if_dict[ip] = interfaces
#         except Exception as e:
#             print(f"无法从 {ip} 获取信息: {e}")
#             device_if_dict[ip] = '无法获取信息'
#
#     return device_if_dict
#
#
# if __name__ == '__main__':
#     pprint.pprint(qytang_get_if('10.10.1.1', '10.10.1.10', username='admin', password='Cisco123'), indent=4)
