import os
import time

from SSH_connection import SSH_connection

class iperf(object, SSH_connection):
    def __init__(self,filename, conf_data, host_index):
        SSH_connection.__init__(self, conf_data, host_index)
        self.__port_iperf = conf_data['port'][host_index]
        self.__master_IP = conf_data['master_ip'][host_index]
        self.__hostname = conf_data['hostname'][host_index]
        self.__username = conf_data['username'][host_index]
        self.__password = conf_data['password'][host_index]
        self.__filename = filename
        self.__port_SSH = 22
        self.__s = None

    def TCP_Download(self):
        self.__s = SSH_connection.connect_to_host(self)
        if self.__s is int:
            return self.__s
        else:
            stdin, stdout, stderr = self.__s.exec_command('iperf -s -i 1 -p %s'
                                  % str(self.__port_iperf))
            time.sleep(3)
            os.system('iperf -c %s -i 1 -p %s |tee %s'
                      % (self.__hostname,
                         str(self.__port_iperf),
                         self.__filename))
            time.sleep(2)
            print ("****************************************************")
            stdin, stdout, stderr = self.__s.exec_command('killall iperf')
            self.__s.close()
            return 0

    def TCP_Upload(self):
        self.__s = SSH_connection.connect_to_host(self)

        if self.__s is int:
            return self.__s
        else:
            os.system('iperf -s -i 1 -p %s | tee %s &'
                      % (str(self.__port_iperf), self.__filename))
            time.sleep(2)
            stdin, stdout, stderr = self.__s.exec_command('iperf -c %s -i 1 -p %s'
                                           % (self.__master_IP,
                                              str(self.__port_iperf)))
            print(stdout.read())
            time.sleep(2)
            print ("****************************************************")
            os.system('killall iperf')
            self.__s.close()
            return 0

    def UDP_Download(self):
        self.__s = SSH_connection.connect_to_host(self)

        if (self.__s == -1):
            return -1
        elif (self.__s == -2):
            return -2
        else:
            stdin, stdout, stderr = self.__s.exec_command('iperf -s -i 1 -u -p %s'
                                  % str(self.__port_iperf))
            time.sleep(3)
            os.system('iperf -c %s -i 1 -u -b 100000000 -p %s |tee %s'
                      % (self.__hostname,
                         str(self.__port_iperf),
                         self.__filename))
            time.sleep(2)
            print ("****************************************************")
            stdin, stdout, stderr = self.__s.exec_command('killall iperf')
            self.__s.close()
            return 0

    def UDP_Upload(self):
        self.__s = SSH_connection.connect_to_host(self)

        if (self.__s == -1):
            return -1
        elif(self.__s == -2):
            return -2
        else:
            os.system('iperf -s -i 1 -u -p %s | tee %s &'
                      % (str(self.__port_iperf), self.__filename))
            time.sleep(2)
            stdin, stdout, stderr = self.__s.exec_command(
                'iperf -c %s -i 1 -u -b 100000000 -p %s'
                % (self.__master_IP, str(self.__port_iperf)))
            print(stdout.read())
            time.sleep(2)
            print ("****************************************************")
            os.system('killall iperf')
            self.__s.close()
            return 0

    def list_parameters(self):
        print(self.__hostname,self.__port_iperf,self.__port_SSH,self.__username,self.__password,self.__master_IP,self.__s)

