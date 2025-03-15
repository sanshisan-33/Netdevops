from datetime import datetime, timedelta

# 获取当前日期和时间
now = datetime.now()

# 计算五天前的日期和时间
five_days_ago = now - timedelta(days=5)

# 格式化五天前的日期和时间
formatted_time = five_days_ago.strftime('%Y-%m-%d %H:%M:%S.%f')

# 创建文件名，使用当前日期和时间
file_name = f"save_fivedayago_time_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# 写入文件
with open(file_name, 'w') as file:
    file.write(formatted_time)

print(f"File '{file_name}'")

from datetime import datetime, timedelta

now = datetime.now()
five_days_ago = now - timedelta(days=5)
formatted_time = five_days_ago.strftime('%Y-%m-%d %H:%M:%S.%f')
file_name = f"save_fivedayago_time_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

with open(file_name, 'w') as file:
    file.write(formatted_time)

print(f"File '{file_name}'")
