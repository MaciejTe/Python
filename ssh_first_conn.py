import subprocess, os, pexpect, tempfile
from iperf_exec import iperf

class ssh_first_conn(iperf):

    def __init__(self,hostname, username, password):
        #self.hostname = hostname
        #self.username = username
        self.password = password
        self.command = 'exit'
        #self.options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
        self.ssh_cmd = 'ssh %s@%s' % (hostname, username)

    def conn(self):
        try:

            child = pexpect.spawn(self.ssh_cmd, timeout=30)
            print('CHUUUUUUUUUUUUUUUUUUUUUUUUJ')
            if child.expect('(yes/no)'):
                child.sendline('yes')
                child.expect(['password:'])
                child.sendline(self.password)
            elif child.expect('authenticity'):
                child.sendline(self.password)
            elif child.expect('password:'):
                child.sendline(self.password)
            elif child.expect('Welcome'):
                child.sendline('ls')
            child.kill()

        except EOFError:
            print('End of file error')
        # except TimeoutError:
        #     print('TimeOut error')



ob = ssh_first_conn('192.168.10.9', 'lukaspolon', 'fullypein2')
ob.conn()