'''
###### ASSUMPTIONS ######

1. Script doesn't set interfaces to be tested - Master has to be LAN client(default eth0 interface), other hosts - Wi-fi(wlan0 interfaces)
2.
'''
import time
#
#
from iperf_exec import iperf
import threading
from iperf_threads import threads_TCP_Download,threads_TCP_Upload
from iperf_threads import threads_UDP_Download,threads_UDP_Upload
from read_config import read_config

class main():
    def __init__(self):
        read = read_config()
        read.start()
        self.__list_hostname = read.get_list_hostname()
        self.__list_username = read.get_list_username()
        self.__list_port = read.get_list_port()
        self.__list_password = read.get_list_password()
        self.__list_master_ip = read.get_list_master_ip()
        
        self.__hosts_number = len(self.__list_hostname)
        #print(self.__list_hostname, self.__list_username, self.__list_port, self.__list_password, self.__list_master_ip)
        self.__list_filenames = []

        for i in range(0,self.__hosts_number):
            self.__list_filenames.append('log%s' % i) 
        #print(self.__list_filenames)

    def one_host(self):
        thread1 = threads_TCP_Download(self.__list_filenames[0], "TCP_D_%s" % str(self.__list_hostname[0]),
                                       self.__list_hostname[0] , self.__list_port[0], self.__list_username[0],
                                       self.__list_password[0], self.__list_master_ip[0])

        thread2 = threads_TCP_Upload(self.__list_filenames[0], "TCP_U_%s" % str(self.__list_hostname[0]),
                                     self.__list_hostname[0], self.__list_port[0], self.__list_username[0],
                                     self.__list_password[0], self.__list_master_ip[0])

        thread3 = threads_UDP_Download(self.__list_filenames[0], "UDP_D_%s" % str(self.__list_hostname[0]),
                                     self.__list_hostname[0], self.__list_port[0], self.__list_username[0],
                                     self.__list_password[0], self.__list_master_ip[0])

        thread4 = threads_UDP_Upload(self.__list_filenames[0], "UDP_U_%s" % str(self.__list_hostname[0]),
                                       self.__list_hostname[0], self.__list_port[0], self.__list_username[0],
                                       self.__list_password[0], self.__list_master_ip[0])

        thread2.start()
        while (len(threading.enumerate()) !=1):
            pass
        thread1.start()
        while (len(threading.enumerate()) != 1):
            pass
        thread4.start()
        while (len(threading.enumerate()) != 1):
            pass
        thread3.start()


    # def multiple_hosts(self):
    #      thread1 = threads_TCP_Upload(self.__list_filenames[1], "TCP_U_%s" % str(self.__list_hostname[1]), self.__list_hostname[1] , self.__list_port[1], self.__list_username[1], self.__list_password[1], self.__list_master_ip[1])
    #      thread1.start()
    #
    # thread1 = threads_TCP_Download(self.__list_filenames[0], "TCP_D_%s" % str(self.__list_hostname[0]),self.__list_hostname[0], self.__list_port[0], self.__list_username[0], self.__list_password[0], self.__list_master_ip[0])
    # thread1.start()

ob = main()
ob.one_host()
