import mock
import unittest

from SshConnection import SshConnection


class TestSshCon(object, unittest.TestCase):
    """Tests SshConnection class from WiFi_perf project"""

    def setUp(self):
        sshcon_mock = mock.MagicMock()
        pass

    def tearDown(self):
        pass

    def test_init(self):
        """Tests __init__ method in SshConnection class"""
        pass

    def test_connect_to_host(self):
        """Tests connect_to_host method in SshConnection class"""
        pass

    def test_connect_to_cpe(self):
        """Tests connect_to_cpe method in SshConnection class"""
        pass


if __name__ == '__main__':
    ob = TestSshCon()
