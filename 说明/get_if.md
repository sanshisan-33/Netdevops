# get_if.py 说明

## 文件概述
该脚本用于通过SSH连接到设备并获取接口的IP地址信息。

## 代码原理
- 使用ssh_paramiko模块进行SSH连接。
- 使用monitor_http模块进行Ping操作。
- 解析设备返回的接口信息。

## 逻辑说明
1. 导入必要的模块：ssh_paramiko、monitor_http、re、pprint。
2. 定义qytang_get_if函数：
   - 对每个IP地址进行Ping测试。
   - 如果可达，使用SSH连接并执行命令获取接口信息。
   - 解析返回结果并存储在字典中。
3. 在主程序中调用qytang_get_if函数并打印结果。

## 步骤逻辑
- 对每个设备IP进行Ping测试。
- 使用SSH连接获取接口信息。
- 解析并打印接口的IP地址。
