# import socket
# import time
#
#
# def check_port(address='10.10.1.200', port=80):
#     """Check if the TCP port is open."""
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.settimeout(1)
#         result = sock.connect_ex((address, port))
#         return result == 0
#
#
# def main():
#     address = '10.10.1.200'  # 要监听的服务器地址
#     port = 80  # 监听的端口号
#
#     print(f"开始监控 {address}:{port} 是否打开...")
#
#     while True:
#         try:
#             if check_port(address, port):
#                 print(f"告警：{address}:{port} 已经被打开！")
#                 break
#             else:
#                 print("等待一秒重新开始监控！")
#         except Exception as e:
#             print(f"发生错误: {e}")
#
#         # 等待一秒
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     main()

# import socket
# import time
#
#
# def open(port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.settimeout(1)  # 设置超时时间为1秒
#         return s.connect_ex(('localhost', port)) == 0
#
#
# while True:
#     if open(80):
#         print("HTTP (TCP/80)服务已经被打开")
#         break
#     else:
#         print("等待一秒重新开始监控!")
#         time.sleep(1)

# print('方案一:不用函数解决')
# list1 = ['aaa', 111, (4, 5), 2.01]
# list2 = ['bbb', 333, 111, 3.14, (4, 5)]
#
# for item in list1:
#     if item not in list2:
#         print(f"{item} only in List1")
#
# for item in list1:
#     if item in list2:
#         print(f"{item} in List1 and List2")
#
# print('方案二:修改为函数的更加通用的方案')
#
#
# def compare_lists(list1, list2):
#     for item in list1:
#         if item not in list2:
#             print(f"{item} only in List1")
#
#     for item in list1:
#         if item in list2:
#             print(f"{item} in List1 and List2")
#
#
# list1 = ['aaa', 111, (4, 5), 2.01]
# list2 = ['bbb', 333, 111, 3.14, (4, 5)]
#
# compare_lists(list1, list2)

from kamene.all import *
import logging
# from scapy.all import *
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()

    ping_result = sr1(ping_pkt, timeout=2, verbose=False)

    if ping_result:

        return ping_result
    else:

        return ping_result


if __name__ == '__main__':
    ip = '192.168.31.204'
    result = qytang_ping(ip)

    if result:
        print(f"{ip} 通")
    else:
        print(f"{ip} 不通")
