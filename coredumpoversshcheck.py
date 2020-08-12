import paramiko,sys

hostname = "94.125.123.255"
password = "visonic1!"

username = "root"
port = 22
command = "ls -l /var/lib/coredumps/"
command2 = 'systemctl status --type service  --all --state running | egrep "Active:" -B3'

def check1(hostname,port,username,password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    client.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command)
    print("Coredump check:")
    for line in iter(stdout.readline, ""):
         print(line, end="")
    client.close()


def check2(hostname,port,username,password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    client.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command2)
    print("Services check:")
    for line in iter(stdout.readline, ""):
        print(line, end="")
    client.close()

#run coredump check
check1(hostname,port,username,password)

#run services check
check2(hostname,port,username,password)

