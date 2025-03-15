import random

def random_ipv4():
    return ".".join(str(random.randint(0, 255)) for a in range(4))


random_ip = random_ipv4()
print("随机生成的IPv4地址:", random_ip)
