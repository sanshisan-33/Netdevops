import paramiko
import argparse


def ssh_connect(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=username, password=password)
        return client
    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")
        return None


def execute_command(client, command):
    if not client:
        print("No valid SSH connection available.")
        return
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode()
    error = stderr.read().decode()
    if error:
        print(f"Error: {error}")
    else:
        print(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ipaddr', required=True, help='SSH Server IP Address')
    parser.add_argument('-u', '--username', default='root', help='SSH Username (default: root)')
    parser.add_argument('-p', '--password', default='qyt123', help='SSH Password (default: qyt123)')
    parser.add_argument('-c', '--command', default='ls', help='Shell Command to Execute (default: ls)')

    args = parser.parse_args()

    ip = args.ipaddr
    username = args.username
    password = args.password
    command = args.command

    client = ssh_connect(ip, username, password)
    execute_command(client, command)
    if client:
        client.close()


if __name__ == '__main__':
    main()
