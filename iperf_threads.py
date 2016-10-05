import threading
from iperf_exec import Iperf
from analyzelog import AnalyzeLog


class threads_TCP_Download(threading.Thread, Iperf):

    def __init__(self, filename, host_index, threadID, conf_data):
        Iperf.__init__(self, filename, conf_data, host_index)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename
        self.__func_state = None

    def run(self):
        print("Starting " + self.__threadID)
        self.__func_state = Iperf.tcp_download(self)
        ob = AnalyzeLog()
        ob.get_mean_value(self.__filename,self.__threadID)
        ob.get_all_data(self.__filename,self.__threadID)

    def get_func_state(self):
        return self.__func_state

class threads_TCP_Upload(threading.Thread, Iperf):
    def __init__(self, filename, host_index, threadID, conf_data):
        Iperf.__init__(self, filename, conf_data, host_index)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename
        self.__func_state = None

    def run(self):
        print("Starting " + self.__threadID)
        self.__func_state = Iperf.tcp_upload(self)
        ob = AnalyzeLog()
        ob.get_mean_value(self.__filename, self.__threadID)
        ob.get_all_data(self.__filename, self.__threadID)

    def get_func_state(self):
        return self.__func_state

class threads_UDP_Download(threading.Thread, Iperf):
    def __init__(self, filename, host_index, threadID, conf_data):
        Iperf.__init__(self, filename, conf_data, host_index)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename
        self.__func_state = None

    def run(self):
        print("Starting " + self.__threadID)
        self.__func_state = Iperf.udp_download(self)
        ob = AnalyzeLog()
        ob.get_mean_value(self.__filename, self.__threadID)
        ob.get_all_data(self.__filename, self.__threadID)

    def get_func_state(self):
        return self.__func_state


class threads_UDP_Upload(threading.Thread, Iperf):
    def __init__(self, filename, host_index, threadID, conf_data):
        Iperf.__init__(self, filename, conf_data, host_index)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename
        self.__func_state = None

    def run(self):
        print("Starting " + self.__threadID)
        self.__func_state = Iperf.udp_upload(self)
        ob = AnalyzeLog()
        ob.get_mean_value(self.__filename, self.__threadID)
        ob.get_all_data(self.__filename, self.__threadID)

    def get_func_state(self):
        return self.__func_state

from SshConnection import SshConnection

class CPE_configuration(threading.Thread, SshConnection):
    def __init__(self, channel, host_index, threadID, conf_data):
        SshConnection.__init__(self, conf_data, host_index)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__channel = channel
        self.__func_state = None

    def run(self):
        print("Starting " + self.__threadID)
        self.__func_state = SshConnection.connect_to_cpe(self, self.__channel)

    def get_func_state(self):
        return self.__func_state


