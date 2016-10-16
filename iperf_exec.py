import os
import time

from SshConnection import SshConnection


class Iperf(SshConnection):
    #GLOBAL
    DEC = ('*' * 52)
    #STATIC
    UDP_BANDWIDTH = '100M'
    DURATION_TIME = '10'

    def __init__(self, filename, conf_data, host_index):
        SshConnection.__init__(self, conf_data, host_index)
        self.__port_iperf = conf_data['Port'][host_index]
        self.__master_IP = conf_data['Master_IP'][0]
        self.__hostname = conf_data['Hostname'][host_index]
        self.__username = conf_data['Username'][host_index]
        self.__password = conf_data['Password'][host_index]
        self.__filename = filename
        self.__port_SSH = 22
        self.__s = None

    def tcp_download(self):
        self.__s = SshConnection.connect_to_host(self)

        if self.__s is None:
            result = self.__s
        else:
            stdin, stdout, stderr = self.__s.exec_command(
                                    'iperf -s -i 1 -p %s'
                                    % str(self.__port_iperf))
            time.sleep(3)
            os.system('iperf -c %s -i 1 -p %s -t %s|tee %s' %
                      (self.__hostname,
                       str(self.__port_iperf),
                       Iperf.DURATION_TIME,
                       self.__filename))

            time.sleep(2)
            print(self.DEC)
            stdin, stdout, stderr = self.__s.exec_command('killall iperf')
            self.__s.close()
            result = 0

        return result

    def tcp_upload(self):
        self.__s = SshConnection.connect_to_host(self)

        if self.__s is None:
            result = self.__s
        else:
            os.system('iperf -s -i 1 -p %s | tee %s &' %
                      (str(self.__port_iperf), self.__filename))
            time.sleep(2)
            stdin, stdout, stderr = self.__s.exec_command(
                                    'iperf -c %s -i 1 -p %s -t %s' %
                                    (self.__master_IP,
                                     str(self.__port_iperf),
                                     Iperf.DURATION_TIME))

            print(stderr.read())
            time.sleep(2)
            print(self.DEC)
            os.system('killall iperf')
            self.__s.close()
            result = 0

        return result

    def udp_download(self):
        self.__s = SshConnection.connect_to_host(self)

        if self.__s is None:
            result = self.__s
        else:
            stdin, stdout, stderr = self.__s.exec_command(
                        'iperf -s -i 1 -u -p %s' % str(self.__port_iperf))

            time.sleep(3)
            os.system('iperf -c %s -i 1 -u -b %s -p %s -t %s|tee %s' %
                     (self.__hostname,
                      Iperf.UDP_BANDWIDTH,
                      str(self.__port_iperf),
                      Iperf.DURATION_TIME,
                      self.__filename))

            time.sleep(2)
            print(self.DEC)
            stdin, stdout, stderr = self.__s.exec_command('killall iperf')
            self.__s.close()
            result = 0

        return result

    def udp_upload(self):
        self.__s = SshConnection.connect_to_host(self)

        if self.__s is None:
            result = self.__s
        else:
            os.system('iperf -s -i 1 -u -p %s | tee %s &' %
                      (str(self.__port_iperf), self.__filename))

            time.sleep(2)
            stdin, stdout, stderr = self.__s.exec_command(
                'iperf -c %s -i 1 -u -b %s -p %s -t %s' %
                (self.__master_IP,
                 Iperf.UDP_BANDWIDTH,
                 str(self.__port_iperf),
                 Iperf.DURATION_TIME))

            print(stdout.read())
            time.sleep(2)
            print (self.DEC)
            os.system('killall iperf')
            self.__s.close()
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
### komentarz