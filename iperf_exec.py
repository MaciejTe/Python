import paramiko, os
import time
from SSH_connection import SSH_connection

class iperf(SSH_connection):
    def __init__(self, filename, hostname, username, password, port_iperf, master_IP):
        SSH_connection.__init__(self,hostname, username,password)
        self.__port_SSH = 22
        self.__port_iperf = port_iperf
        self.__master_IP = master_IP
        self.__hostname = hostname
        self.__username = username
        self.__password = password
        self.__s = None
        self.__filename = filename

    def TCP_Download(self):
        #print(SSH_connection.get_paramiko_object(self))
        #self.list_parameters()
        self.__s = SSH_connection.connect_to_host(self)
        stdin, stdout, stderr = self.__s.exec_command('iperf -s -i 1 -p %s' % str(self.__port_iperf))
        time.sleep(3)
        os.system('iperf -c %s -i 1 -p %s |tee %s' % (self.__hostname, str(self.__port_iperf), self.__filename))
        time.sleep(2)
        print ("****************************************************")
        stdin, stdout, stderr = self.__s.exec_command('killall iperf')
        self.__s.close()
        #stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')

    def TCP_Upload(self):
        self.__s = SSH_connection.connect_to_host(self)
        os.system('iperf -s -i 1 -p %s | tee %s &' % (str(self.__port_iperf), self.__filename))
        time.sleep(2)
        stdin, stdout, stderr = self.__s.exec_command('iperf -c %s -i 1 -p %s' % (self.__master_IP, str(self.__port_iperf)))
        print(stdout.read())
        time.sleep(2)
        print ("****************************************************")
        os.system('killall iperf')
        self.__s.close()
        #stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')
        #os.system('ps ax|grep iperf')

    def UDP_Download(self):
        self.__s = SSH_connection.connect_to_host(self)
        stdin, stdout, stderr = self.__s.exec_command('iperf -s -i 1 -u -p %s' % str(self.__port_iperf))
        time.sleep(3)
        os.system('iperf -c %s -i 1 -u -b 100000000 -p %s |tee %s' % (self.__hostname, str(self.__port_iperf), self.__filename))
        time.sleep(2)
        print ("****************************************************")
        stdin, stdout, stderr = self.__s.exec_command('killall iperf')
        self.__s.close()
        # stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')

    def UDP_Upload(self):
        self.__s = SSH_connection.connect_to_host(self)
        os.system('iperf -s -i 1 -u -p %s | tee %s &' % (str(self.__port_iperf), self.__filename))
        time.sleep(2)
        stdin, stdout, stderr = self.__s.exec_command(
            'iperf -c %s -i 1 -u -b 100000000 -p %s' % (self.__master_IP, str(self.__port_iperf)))
        print(stdout.read())
        time.sleep(2)
        print ("****************************************************")
        os.system('killall iperf')
        self.__s.close()
        # stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')

    def list_parameters(self):
        print(self.__hostname,self.__port_iperf,self.__port_SSH,self.__username,self.__password,self.__master_IP,self.__s)


#ob = iperf('192.168.10.5','maciek','eysuaaty', 50000,'192.168.10.10')
#ob.UDP_Upload()
# ob.close_SSH_connection()
