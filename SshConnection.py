import paramiko
import time
from paramiko.ssh_exception import *


class SshConnection(object):
    PARAMIKO_FILE = 'paramiko.log'

    def __init__(self,__conf_data, host_index):
        self.__hostname = __conf_data['hostname'][host_index]
        self.__username = __conf_data['username'][host_index]
        self.__password = __conf_data['password'][host_index]
        self.__CPE_hostname = __conf_data['CPE_credentials'][0]
        self.__CPE_username = __conf_data['CPE_credentials'][1]
        self.__CPE_password = __conf_data['CPE_credentials'][2]
        self.__port_SSH = 22
        self.__ssh = None
        self.__s = None

    def connect_to_host(self):
        try:
            paramiko.util.log_to_file(self.PARAMIKO_FILE)
            self.__s = paramiko.SSHClient()
            self.__s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.__s.load_system_host_keys()
            self.__s.connect(self.__hostname, self.__port_SSH,
                             self.__username, self.__password)
            return self.__s

        except BadAuthenticationType:
            print('bad_auth')
            self.__s.close()
            return 101
        except AuthenticationException:
            print('auth_exc')
            self.__s.close()
            return 102
        except Exception as e:
            print(e)
            self.__s.close()
            return 103

    def connect_to_cpe(self, channel):
        connection = None  # ????????

        try:
            paramiko.util.log_to_file(self.PARAMIKO_FILE)
            connection = paramiko.SSHClient()
            connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            connection.load_system_host_keys()
            connection.connect(self.__CPE_hostname, self.__port_SSH,
                               self.__CPE_username, self.__CPE_password)
            self.__ssh = connection.invoke_shell()

            output = self.__ssh.recv(10000)
            print(output)

            time.sleep(4)
            self.__ssh.send('\n' + 'interface wifi24ghz channel %s'
                            % channel + '\n')
            output = self.__ssh.recv(50000)
            print(output)
            time.sleep(1)
            self.__ssh.send('\n' + 'co pr bo\n')
            output = self.__ssh.recv(50000)
            time.sleep(6)
            self.__ssh.send('\n' + 'exit\n')
            connection.close()
            print(output)
            return 0

        except AuthenticationException:
            print('Incorrect username or password for CPE')
            connection.close()
            return 104
        except Exception as e:
            print(e)
            connection.close()
            return 105

    def get_paramiko_object(self):
        return self.__s





