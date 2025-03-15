import paramiko
import argparse

def ssh_connect(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password)
    return client

def execute_command(client, command):
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
    parser.add_argument('-u', '--username', required=True, help='SSH Username')
    parser.add_argument('-p', '--password', required=True, help='SSH Password')
    parser.add_argument('-c', '--command', default='ls', help='Shell Command to Execute')

    args = parser.parse_args()

    ip = args.ipaddr
    username = args.username
    password = args.password
    command = args.command

    try:
        client = ssh_connect(ip, username, password)
        execute_command(client, command)
        client.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()