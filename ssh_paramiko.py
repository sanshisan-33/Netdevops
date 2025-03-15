import paramiko
import re


def qytang_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(ip, username=username, password=password, port=port, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    ssh.close()
    if x:
        return x


def ssh_get_route(ip, username, password, port=22):
    route1 = qytang_ssh(ip, username, password, cmd='route -n')
    Gateway_pattern = r'^\S+\s+(\d+\.\d+\.\d+\.\d+)\s+\S+\s+UG'
    math = re.findall(Gateway_pattern, route1, re.MULTILINE)[0]

    if math:
        return math


if __name__ == '__main__':
    print(qytang_ssh('10.10.1.200', 'root', 'qyt123'))
    print(qytang_ssh('10.10.1.200', 'root', 'qyt123', cmd='pwd'))
    print('网关为：')
    print(ssh_get_route('10.10.1.200', 'root', 'qyt123'))
