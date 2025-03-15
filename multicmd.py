import paramiko
import time


def read_until_prompt(chan, prompt='#', timeout=10):
    response = ''
    start_time = time.time()

    while True:
        if chan.recv_ready():
            chunk = chan.recv(2048).decode()
            response += chunk

            if prompt in chunk or '%' in chunk:
                break

            if '--More--' in chunk:
                chan.send(' ')
                time.sleep(0.5)  #

        if time.time() - start_time > timeout:
            print("读取超时")
            break

    return response


def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:

        ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)

        chan = ssh.invoke_shell()
        time.sleep(wait_time)

        initial_response = read_until_prompt(chan)
        if verbose:
            print(initial_response)

        if enable:
            chan.send('enable\n'.encode())
            time.sleep(wait_time)
            initial_response = read_until_prompt(chan)
            if verbose:
                print(initial_response)
            chan.send((enable + '\n').encode())
            time.sleep(wait_time)
            initial_response = read_until_prompt(chan)
            if verbose:
                print(initial_response)

        for cmd in cmd_list:
            chan.send((cmd + '\n').encode())
            time.sleep(wait_time)

            response = read_until_prompt(chan)
            if verbose:
                print(response)

    except Exception as e:
        print(f"发生错误: {e}")
    finally:

        ssh.close()


if __name__ == '__main__':
    commands = [
        'show version',
        'show run',
        'configure terminal',
        'router ospf 1',
        'network 192.168.1.0 0.0.0.255 area 0',
        'end'
    ]
    qytang_multicmd(
        ip='192.168.1.1',
        username='admin',
        password='Cisco123',
        cmd_list=commands,
        enable='',
        wait_time=2,
        verbose=True
    )
