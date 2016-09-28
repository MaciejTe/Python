import paramiko
import time
from paramiko.ssh_exception import *


class SshConnection(object):
    """Class for create SSH connection with hosts and CPE"""

    # GLOBAL CONSTANTS
    PARAMIKO_FILE = 'paramiko.log'

    def __init__(self, conf_data, host_index):
        """Set up the necessary credentials

        Args:
            conf_data (dict): set up data
            host_index (int): number that identifies host

        """

        self.hostname = conf_data['hostname'][host_index]
        self.username = conf_data['username'][host_index]
        self.password = conf_data['password'][host_index]
        self.CPE_hostname = conf_data['CPE_credentials'][0]
        self.CPE_username = conf_data['CPE_credentials'][1]
        self.CPE_password = conf_data['CPE_credentials'][2]
        self.port_SSH = 22
        self.ssh = None
        self.s = None

    def connect_to_host(self):
        """Set the ssh connection for host.

        Returns:
            result: Paramiko object for success,
                    error code (int) otherwise.

        """

        try:
            paramiko.util.log_to_file(self.PARAMIKO_FILE)
            self.s = paramiko.SSHClient()
            self.s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.s.load_system_host_keys()
            self.s.connect(self.hostname, self.port_SSH,
                           self.username, self.password)
            result = self.s

        except BadAuthenticationType:
            print('bad_auth')
            result = 101
        except AuthenticationException:
            print('auth_exc')
            result = 102
        except Exception as e:
            print(e)
            result = 103
        finally:
            self.s.close()

        return result

    def connect_to_cpe(self, channel):
        """Set the ssh connection for CPE

        Args:
            channel (int): router channel

        Returns:
            result: 0 (int) for success,
                    error code (int) otherwise.

        """
        connection = None  # ????????

        try:
            paramiko.util.log_to_file(self.PARAMIKO_FILE)
            connection = paramiko.SSHClient()
            connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            connection.load_system_host_keys()
            connection.connect(self.CPE_hostname, self.port_SSH,
                               self.CPE_username, self.CPE_password)
            self.ssh = connection.invoke_shell()

            output = self.ssh.recv(10000)
            print(output)

            time.sleep(4)
            self.ssh.send('\n' + 'interface wifi24ghz channel %s'
                          % channel + '\n')
            output = self.ssh.recv(50000)
            print(output)
            time.sleep(1)
            self.ssh.send('\n' + 'co pr bo\n')
            output = self.ssh.recv(50000)
            time.sleep(6)
            self.ssh.send('\n' + 'exit\n')
            print(output)
            result = 0
            connection.close()

        except AuthenticationException:
            print('Incorrect username or password for CPE')
            result = 104
            connection.close()
        except Exception as e:
            print(e)
            result = 105
            connection.close()
        # finally:
        #     connection.close()

        return result







