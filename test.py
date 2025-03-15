# # \t是制表符Tab
# print('今天\t开始')
# # \n是换行
# print('今天开\n始')
# # \\是输出\
# print('今\\天\\\\开\\始')
# # \"是输出"  同理\'是输出'
# print('今\"天\'开\"始')
# # \r是输出回车，会覆盖前面输出的内容
# print('今天啊\r开始')


# print("姓名\t年龄\t籍贯\t住址\ntom\t12\t河北\t北京")
# 定义了一个变量，变量的名称a，变量的值是1，1是int类型(整数类型)
# a = 1
# # 定义了一个变量，变量的名称b，变量的值是2，2是int类型(整数类型)
# b = 2
# # 变量b的值修改成8，变量b的值就是8，8是int类型。
# b = 8
#
# # 输出变量的值，type(a)表示输出a的类型
# print("a的值是", a, "类型是", type(a))
# print("b的值是", b, "类型是", type(b))


#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# from http.server import HTTPServer, CGIHTTPRequestHandler
# port = 80
# httpd = HTTPServer(('',port), CGIHTTPRequestHandler)
# print('Starting simple httpd on port: ' + str(httpd.server_port))
# httpd.serve_forever()

from kamene.all import *
import logging

# 减少Kamene的输出信息
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

# 正确实例化IP和ICMP层，并使用斜杠连接
ping_pkt = IP(dst='196.21.5.254') / ICMP()

# 发送数据包并接收响应
ping_result = sr1(ping_pkt, timeout=2, verbose=False)

if ping_result:
    ping_result.show()  # 显示接收到的数据包详情
else:
    print("没有收到回复")

