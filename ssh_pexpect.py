from pexpect import pxssh
import getpass
try:
    s = pxssh.pxssh(options={ \
                    "StrictHostKeyChecking": "no", \
                    "UserKnownHostsFile": "/dev/null"})

    s.login('192.168.10.9', 'lukaspolon', 'fullypein2')
    s.sendline('uptime')   # run a command
    s.prompt()             # match the prompt
    print(s.before)        # print everything before the prompt.

    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)


class ssh():
    def __init__(self):
