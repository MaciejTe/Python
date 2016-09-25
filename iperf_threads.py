import threading
from iperf_exec import iperf
from analyzelog import AnalyzeLog

class threads_TCP_Download(threading.Thread,iperf):

    def __init__(self,filename, threadID,hostname,port_iperf,username,password,master_IP):
        iperf.__init__(self,filename, hostname,username,password,port_iperf, master_IP)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename
        self.__func_state = None

    def run(self):
        print("Starting " + self.__threadID)
        self.__func_state = iperf.TCP_Download(self)
        ob = AnalyzeLog()
        ob.get_mean_value(self.__filename,self.__threadID)
        ob.get_all_data(self.__filename,self.__threadID)

    def get_func_state(self):
        return self.__func_state

class threads_TCP_Upload(threading.Thread,iperf):
    def __init__(self,filename, threadID,hostname,port_iperf,username,password,master_IP):
        iperf.__init__(self,filename, hostname,username, password, port_iperf,master_IP)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename
        self.__func_state = None

    def run(self):
        print("Starting " + self.__threadID)
        self.__func_state = iperf.TCP_Upload(self)
        ob = AnalyzeLog()
        ob.get_mean_value(self.__filename, self.__threadID)
        ob.get_all_data(self.__filename, self.__threadID)

    def get_func_state(self):
        return self.__func_state

class threads_UDP_Download(threading.Thread,iperf):
    def __init__(self,filename,threadID,hostname,port_iperf,username,password,master_IP):
        iperf.__init__(self,filename, hostname,username, password, port_iperf,master_IP)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename
        self.__func_state = None

    def run(self):
        print("Starting " + self.__threadID)
        self.__func_state = iperf.UDP_Download(self)
        ob = AnalyzeLog()
        ob.get_mean_value(self.__filename, self.__threadID)
        ob.get_all_data(self.__filename, self.__threadID)

    def get_func_state(self):
        return self.__func_state


class threads_UDP_Upload(threading.Thread,iperf):
    def __init__(self,filename,threadID,hostname,port_iperf,username,password,master_IP):
        iperf.__init__(self,filename, hostname,username, password, port_iperf,master_IP)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename
        self.__func_state = None

    def run(self):
        print("Starting " + self.__threadID)
        self.__func_state = iperf.UDP_Upload(self)
        ob = AnalyzeLog()
        ob.get_mean_value(self.__filename, self.__threadID)
        ob.get_all_data(self.__filename, self.__threadID)

    def get_func_state(self):
        return self.__func_state

from SSH_connection import SSH_connection

class CPE_configuration(threading.Thread,SSH_connection):
    def __init__(self, channel, threadID, hostname, username, password):
        SSH_connection.__init__(self,hostname, username,password)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__channel = channel
        self.__func_state = None

    def run(self):
        print("Starting " + self.__threadID)
        self.__func_state = SSH_connection.connect_to_CPE(self,self.__channel)

    def get_func_state(self):
        return self.__func_state


