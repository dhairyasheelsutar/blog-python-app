from scp import SCPClient
import sys
import paramiko

host = sys.argv[1]

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host)

scp = SCPClient(ssh.get_transport())

scp.put('/home/ubuntu/blog-python-app', recursive=True, remote_path='/home/user/blog-python-app')
scp.close()