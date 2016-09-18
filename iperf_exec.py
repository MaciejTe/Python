import os, time, re
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

        if(type(self.__s) == type(1)):
            return self.__s
        else:
            stdin, stdout, stderr = self.__s.exec_command('iperf -s -i 1 -p %s' % str(self.__port_iperf))
            time.sleep(3)
            os.system('iperf -c %s -i 1 -p %s |tee %s' % (self.__hostname, str(self.__port_iperf), self.__filename))
            time.sleep(2)
            print ("****************************************************")
            stdin, stdout, stderr = self.__s.exec_command('killall iperf')
            self.__s.close()
            #stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')
            return 0

    def TCP_Upload(self):
        self.__s = SSH_connection.connect_to_host(self)

        if (type(self.__s) == type(1)):
            return self.__s
        else:
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
            return 0

    def UDP_Download(self):
        self.__s = SSH_connection.connect_to_host(self)

        if (self.__s == -1):
            return -1
        elif (self.__s == -2):
            return -2
        else:
            stdin, stdout, stderr = self.__s.exec_command('iperf -s -i 1 -u -p %s' % str(self.__port_iperf))
            time.sleep(3)
            os.system('iperf -c %s -i 1 -u -b 200M -p %s |tee %s' % (self.__hostname, str(self.__port_iperf), self.__filename))
            time.sleep(2)
            print ("****************************************************")
            stdin, stdout, stderr = self.__s.exec_command('killall iperf')
            self.__s.close()
            # stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')
            return 0

    def UDP_Upload(self):
        self.__s = SSH_connection.connect_to_host(self)

        if (self.__s == -1):
            return -1
        elif(self.__s == -2):
            return -2
        else:
            os.system('iperf -s -i 1 -u -p %s | tee %s &' % (str(self.__port_iperf), self.__filename))
            time.sleep(2)
            stdin, stdout, stderr = self.__s.exec_command(
                'iperf -c %s -i 1 -u -b 200M -p %s' % (self.__master_IP, str(self.__port_iperf)))
            print(stdout.read())
            time.sleep(2)
            print ("****************************************************")
            os.system('killall iperf')
            self.__s.close()
            # stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')
            return 0

    def list_parameters(self):
        print(self.__hostname,self.__port_iperf,self.__port_SSH,self.__username,self.__password,self.__master_IP,self.__s)

