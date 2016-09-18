import threading
from iperf_exec import iperf
from analyze_log import analyze_log

class threads_TCP_Download(threading.Thread,iperf):

    def __init__(self,filename, threadID,hostname,port_iperf,username,password,master_IP):
        iperf.__init__(self,filename, hostname,username,password,port_iperf, master_IP)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename

    def run(self):
        print "Starting " + self.__threadID
        iperf.TCP_Download(self)
        ob = analyze_log()
        ob.get_mean_value(self.__filename,self.__threadID)

class threads_TCP_Upload(threading.Thread,iperf):
    def __init__(self,filename, threadID,hostname,port_iperf,username,password,master_IP):
        iperf.__init__(self,filename, hostname,username, password, port_iperf,master_IP)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename

    def run(self):
        print "Starting " + self.__threadID
        iperf.TCP_Upload(self)
        ob = analyze_log()
        ob.get_mean_value(self.__filename, self.__threadID)

class threads_UDP_Download(threading.Thread,iperf):
    def __init__(self,filename,threadID,hostname,port_iperf,username,password,master_IP):
        iperf.__init__(self,filename, hostname,username, password, port_iperf,master_IP)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename

    def run(self):
        print "Starting " + self.__threadID
        iperf.UDP_Download(self)
        ob = analyze_log()
        ob.get_mean_value(self.__filename, self.__threadID)


class threads_UDP_Upload(threading.Thread,iperf):
    def __init__(self,filename,threadID,hostname,port_iperf,username,password,master_IP):
        iperf.__init__(self,filename, hostname,username, password, port_iperf,master_IP)
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__filename = filename

    def run(self):
        print "Starting " + self.__threadID
        iperf.UDP_Upload(self)
        ob = analyze_log()
        ob.get_mean_value(self.__filename, self.__threadID)
