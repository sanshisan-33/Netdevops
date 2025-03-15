from ssh_paramiko import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip, username='admin', password='Cisco123'):
    try:

        result = qytang_ssh(ip, username=username, password=password, cmd='show run')

        match = re.search(r'(hostname.*?end)', result, re.DOTALL)
        if match:
            config = match.group(1)
            return config
        else:
            print('显示错误')
            return None

    except Exception:
        print('异常')
        return None


def qytang_check_diff(ip, username='admin', password='Cisco123'):
    before_md5 = ''
    change = ''
    while True:
        config = qytang_get_config(ip, username, password)
        if config is not None:
            md5 = hashlib.md5()
            md5.update(config.encode())
            now_md5 = md5.hexdigest()
            print(now_md5)

            if before_md5 and before_md5 != now_md5:
                print('MD5 value changed')
                # sys.exit()
                change = True
                break

            before_md5 = now_md5

        time.sleep(5)

    if change:
        return


if __name__ == '__main__':
    qytang_check_diff('10.10.1.1', username='admin', password='Cisco123')
