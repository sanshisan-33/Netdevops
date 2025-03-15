# import re
# import os
#
# def get_default_gateway():
#     try:
#         route_output = os.popen("route -n").read()
#         # 正则表达式：通过子网掩码和 UG 标志匹配默认网关
#         pattern = re.compile(
#             r'^\s*\S+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0\.0\.0\.0\s+[^\s]*UG[^\s]*\s+.*$',
#             re.MULTILINE
#         )
#         match = pattern.search(route_output)
#         if match:
#             gateway = match.group(1)
#             # 排除保留地址（如 127.0.0.1 或 169.254.0.0/16）
#             if not (re.match(r'^127\.', gateway) or re.match(r'^169\.254', gateway)):
#                 return gateway
#             else:
#                 print("检测到保留地址，跳过...")
#                 return None
#         else:
#             print("未找到默认网关")
#             return None
#     except Exception as e:
#         print(f"发生错误: {e}")
#         return None
#
# # 调用函数
# gateway = get_default_gateway()
# print(f"默认网关: {gateway}")
#

import re
import os

# 执行命令并获取输出
output = os.popen("route -n").read()

# 正则表达式精准匹配
match = re.search(r'0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+)\s+0\.0\.0\.0.*UG', output)

# 直接输出结果
print(f'默认网关: {match.group(1)}')
