import paramiko
import time

class SSH_connection():
    def __init__(self,hostname, username,password):
        self.__hostname = hostname
        self.__port_SSH = 22
        self.__username = username
        self.__password = password
        self.__ssh = None
        self.__s = None


    def connect_to_host(self):
        paramiko.util.log_to_file('paramiko.log')
        self.__s = paramiko.SSHClient()
        self.__s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__s.load_system_host_keys()
        self.__s.connect(self.__hostname, self.__port_SSH, self.__username, self.__password)
        return self.__s

    def connect_to_CPE(self):
        paramiko.util.log_to_file('paramiko.log')
        self.s = paramiko.SSHClient()
        self.s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.s.load_system_host_keys()
        self.s.connect(self.__hostname, self.__port_SSH, self.__username, self.__password)
        self.__ssh = self.s.invoke_shell()

    def send_command_CPE(self, channel):
        output = self.__ssh.recv(10000)
        print output

        time.sleep(4)
        self.__ssh.send('\n' + 'voip id %s disable' % (channel) + '\n')
        output = self.__ssh.recv(50000)
        print output
        time.sleep(1)
        self.__ssh.send('\n' + 'co pr bo\n')
        output = self.__ssh.recv(50000)
        print output

    def get_paramiko_object(self):
        return self.__s


#ob = SSH_connection('192.168.0.15','admin','123')
#ob.connect_to_CPE()
#ob.send_command_CPE('1')

# ob = SSH_connection('192.168.0.15','admin','123')
# print (threading.enumerate())
# ob.s.close()
# print (threading.enumerate())
