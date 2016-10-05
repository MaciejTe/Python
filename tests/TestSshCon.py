from types import NoneType

import mock
import unittest
import sys

sys.path.insert(0, 'C:\Users\LukaszP\Documents\Repos\WiFi_perf')

from SshConnection import SshConnection
from SshConnection import paramiko

from paramiko.ssh_exception import *


class TestSshCon(unittest.TestCase):
    """Tests SshConnection class from WiFi_perf project"""

    def setUp(self):
        self.sshmock = mock.MagicMock(name='ssh', spec=SshConnection)
        self.paramikomock = mock.MagicMock(name='param', spec=paramiko)

        self.hostname = '192.168.10.9'
        self.username = 'lukaspolon'
        self.password = 'abc'
        self.CPE_hostname = '192.168.0.2'
        self.CPE_username = 'bbb'
        self.CPE_password = 'ccc'
        self.port_SSH = 22
        self.ssh = None
        self.s = None

        self.conf_data = {
            'Hostname': [self.hostname],
            'Username': [self.username],
            'Port': ['50000'],
            'Password': [self.password],
            'Master_ip': ['192.168.3.3'],
            'CPE_credentials': [self.CPE_hostname,
                                self.CPE_username,
                                self.CPE_password],
            'Channels': ['1', '9', '13']
        }
        self.host_index = 0
        self.paramiko_file = 'paramiko.log'

    def tearDown(self):
        self.sshmock.reset_mock()
        self.paramikomock.reset_mock()

    def test_init(self):
        """Tests __init__ method in SshConnection class"""

        sshcon = SshConnection(self.conf_data, self.host_index)

        self.assertEqual(sshcon.hostname, self.hostname)
        self.assertEqual(sshcon.username, self.username)
        self.assertEqual(sshcon.password, self.password)
        self.assertEqual(sshcon.CPE_hostname, self.CPE_hostname)
        self.assertEqual(sshcon.CPE_username, self.CPE_username)
        self.assertEqual(type(sshcon.port_SSH), int)
        self.assertEqual(type(sshcon.ssh), NoneType)
        self.assertEqual(type(sshcon.s), NoneType)

    def test_connect_to_host(self):
        """Tests connect_to_host method in SshConnection class"""
        with SshConnection.connect_to_host(self.sshmock) as x:
            pass

    def test_connect_to_cpe(self):
        """Tests connect_to_cpe method in SshConnection class"""
        pass


if __name__ == '__main__':
    unittest.main()
