import os
import time

from SshConnection import SshConnection


class Iperf(SshConnection):
    DECORATOR = "****************************************************"
    #DECORATOR = ('*' * 52)

    def __init__(self, filename, conf_data, host_index):
        SshConnection.__init__(self, conf_data, host_index)
        self.__port_iperf = conf_data['Port'][host_index]
        self.__master_IP = conf_data['Master_IP'][host_index]
        self.__hostname = conf_data['Hostname'][host_index]
        self.__username = conf_data['Username'][host_index]
        self.__password = conf_data['Password'][host_index]
        self.__filename = filename
        self.__port_SSH = 22
        self.__s = None

    def tcp_download(self):
        self.__s = SshConnection.connect_to_host(self)

        if type(self.__s) is int:
            result = self.__s
        else:
            stdin, stdout, stderr = self.__s.exec_command('iperf -s -i 1 -p '
                                                          '%s' %str(self.__port_iperf))
            time.sleep(3)
            os.system('iperf -c %s -i 1 -p %s |tee %s' %(self.__hostname, str(self.__port_iperf), self.__filename))

            time.sleep(2)
            print(self.DECORATOR)
            stdin, stdout, stderr = self.__s.exec_command('killall iperf')
            self.__s.close()
            # stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')
            result = 0

        return result

    def tcp_upload(self):
        self.__s = SshConnection.connect_to_host(self)

        if type(self.__s) is int:
            result = self.__s
        else:
            os.system('iperf -s -i 1 -p %s | tee %s &' %
                      (str(self.__port_iperf), self.__filename))
            time.sleep(2)
            stdin, stdout, stderr = self.__s.exec_command('iperf -c %s -i 1 -p %s' %(self.__master_IP, str(self.__port_iperf)))

            #print(stdout.read())
            print(stderr.read())
            time.sleep(2)
            print(self.DECORATOR)
            print('*******  CHUJ ****************')
            os.system('killall iperf')
            self.__s.close()
            # stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')
            # os.system('ps ax|grep iperf')
            result = 0

        return result

    def udp_download(self):
        self.__s = SshConnection.connect_to_host(self)

        if self.__s is -1:
            result =  -1
        elif self.__s is -2:
            result =  -2
        else:
            stdin, stdout, stderr = self.__s.exec_command(
                        'iperf -s -i 1 -u -p %s' % str(self.__port_iperf))

            time.sleep(3)
            os.system('iperf -c %s -i 1 -u -b 200M -p %s |tee %s' %
                     (self.__hostname,
                      str(self.__port_iperf),
                      self.__filename))

            time.sleep(2)
            print(self.DECORATOR)
            stdin, stdout, stderr = self.__s.exec_command('killall iperf')
            self.__s.close()
            # stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')
            result = 0

        return result

    def udp_upload(self):
        self.__s = SshConnection.connect_to_host(self)

        if self.__s is -1:
            result = -1
        elif self.__s is -2:
            result = -2
        else:
            os.system('iperf -s -i 1 -u -p %s | tee %s &' %
                      (str(self.__port_iperf), self.__filename))

            time.sleep(2)
            stdin, stdout, stderr = self.__s.exec_command(
                'iperf -c %s -i 1 -u -b 200M -p %s' %
                (self.__master_IP, str(self.__port_iperf)))

            print(stdout.read())
            time.sleep(2)
            print (self.DECORATOR)
            os.system('killall iperf')
            self.__s.close()
            # stdin, stdout, stderr = self.s.exec_command('ps ax|grep iperf')
            result = 0

        return result

    def list_parameters(self):
        print(self.__hostname,
              self.__port_iperf,
              self.__port_SSH,
              self.__username,
              self.__password,
              self.__master_IP,
              self.__s)


# from configuration import Configuration
# b = Configuration()
# x = Iperf('log0', b.conf_data, 0)
# x.tcp_upload()