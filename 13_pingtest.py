# from netmiko import ConnectHandler
# import re
#
# # 设备信息
# router = {
#     "device_type": "cisco_ios",
#     "host": "10.10.1.1",  # 替换为你的路由器 IP
#     "username": "admin",  # 替换为你的 SSH 用户名
#     "password": "Cisco123",  # 替换为你的 SSH 密码
#     "secret": "",  # enable 密码
# }
#
#
# class QYTPING:
#     def __init__(self, dst_ip):
#         self.dst_ip = dst_ip
#         self.length = 100  # 默认数据包大小
#         self.scrip = None  # 默认源 IP
#
#     def __str__(self):
#         src_info = f"srcip: {self.scrip}, " if self.scrip else ""
#         return f"<QYTPING => {src_info}dstip: {self.dst_ip}, size: {self.length}>"
#
#     def ping(self, single=False):
#         """ 使用 netmiko 在路由器上执行 ping 并解析输出 """
#         try:
#             connection = ConnectHandler(**router)
#             connection.enable()
#
#             # 生成 ping 命令
#             ping_cmd = f"ping {self.dst_ip} repeat 1" if single else f"ping {self.dst_ip} repeat 5 size {self.length}"
#             if self.scrip:
#                 ping_cmd += f" source {self.scrip}"
#
#             output = connection.send_command(ping_cmd)
#
#             # 解析 ping 结果
#             match = re.findall(r"[!.]", output)
#             if match:
#                 if single:
#                     print(f"{self.dst_ip} 可达！")
#                 else:
#                     print("".join(["!" if char == "!" else "" for char in match]))  # 只输出 `!`
#             else:
#                 print(".....")  # 确保失败时输出 `.....`
#
#             connection.disconnect()
#         except Exception:
#             print(".....")  # 失败时统一返回 `.....`
#
#
# # 修正 NewPing 类
# class NewPing(QYTPING):
#     def ping(self):
#         """ 重写 ping 方法，输出 `+` 代替 `!` """
#         try:
#             connection = ConnectHandler(**router)
#             connection.enable()
#
#             ping_cmd = f"ping {self.dst_ip} repeat 5 size {self.length}"
#             if self.scrip:
#                 ping_cmd += f" source {self.scrip}"
#
#             output = connection.send_command(ping_cmd)
#
#             match = re.findall(r"[!.]", output)
#             if match:
#                 print("".join(["+" if char == "!" else "" for char in match]))  # 只输出 `+`
#             else:
#                 print(".....")
#
#             connection.disconnect()
#         except Exception:
#             print(".....")
#
#
# if __name__ == '__main__':
#     ping = QYTPING('192.168.1.1')  # 使用 QYTPING 类
#     total_len = 70
#
#
#     def print_new(word, s='-'):
#         print('{0}{1}{2}'.format(s * int((70 - len(word)) / 2), word, s * int((70 - len(word)) / 2)))
#
#
#     print_new('print class')
#     print(ping)
#
#     print_new('ping one for sure reachable')
#     ping.ping(single=True)
#
#     print_new('ping five')
#     ping.ping()
#
#     print_new('set payload length')
#     ping.length = 200
#     print(ping)
#     ping.ping()
#
#     print_new('set ping src ip address')
#     ping.scrip = '192.168.1.123'
#     print(ping)
#     ping.ping()  # 这里确保 srcip 不可达时输出 `.....`
#
#     print_new('new class NewPing', '=')
#     newping = NewPing('192.168.1.1')  # 修正 NewPing 类
#     newping.length = 300
#     print(newping)
#     newping.ping()


from netmiko import ConnectHandler
import re

router = {
    "device_type": "cisco_ios",
    "host": "10.10.1.1",
    "username": "admin",
    "password": "Cisco123",
    "secret": "",
}

class QYTPING:
    def __init__(self, dst_ip):
        self.dst_ip = dst_ip
        self.length = 100
        self.scrip = None

    def __str__(self):
        src_info = f"srcip: {self.scrip}, " if self.scrip else ""
        return f"<QYTPING => {src_info}dstip: {self.dst_ip}, size: {self.length}>"

    def ping(self, single=False):
        try:
            connection = ConnectHandler(**router)
            connection.enable()

            ping_cmd = f"ping {self.dst_ip} repeat 1" if single else f"ping {self.dst_ip} repeat 5 size {self.length}"
            if self.scrip:
                ping_cmd += f" source {self.scrip}"

            output = connection.send_command(ping_cmd)

            match = re.findall(r"[!.]", output)
            if match:
                if single:
                    print(f"{self.dst_ip} 可达！")
                else:
                    print("".join(["!" if char == "!" else "" for char in match]))
            else:
                print(".....")

            connection.disconnect()
        except Exception:
            print(".....")


class NewPing(QYTPING):
    def ping(self):
        try:
            connection = ConnectHandler(**router)
            connection.enable()

            ping_cmd = f"ping {self.dst_ip} repeat 5 size {self.length}"
            if self.scrip:
                ping_cmd += f" source {self.scrip}"

            output = connection.send_command(ping_cmd)

            match = re.findall(r"[!.]", output)
            if match:
                print("".join(["+" if char == "!" else "" for char in match]))
            else:
                print(".....")

            connection.disconnect()
        except Exception:
            print(".....")


if __name__ == '__main__':
    ping = QYTPING('192.168.1.1')
    total_len = 70
    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word)) / 2), word, s * int((70 - len(word)) / 2)))

    print_new('print class')
    print(ping)

    print_new('ping one for sure reachable')
    ping.ping(single=True)

    print_new('ping five')
    ping.ping()

    print_new('set payload length')
    ping.length = 200
    print(ping)
    ping.ping()

    print_new('set ping src ip address')
    ping.scrip = '192.168.1.123'
    print(ping)
    ping.ping()

    print_new('new class NewPing', '=')
    newping = NewPing('192.168.1.1')
    newping.length = 300
    print(newping)
    newping.ping()