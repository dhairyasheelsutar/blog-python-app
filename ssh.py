from scp import SCPClient
import sys
import paramiko

host = sys.argv[1]

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(host)

scp.put('/home/ubuntu/blog-python-app', recursive=True, remote_path='/home/user/blog-python-app')
scp.close()