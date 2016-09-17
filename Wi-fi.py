
import time, threading
from iperf_threads import threads_TCP_Download,threads_TCP_Upload
from iperf_threads import threads_UDP_Download,threads_UDP_Upload, CPE_configuration
from read_config import read_config
from Error_handler import Error_handler

class main():
    def __init__(self):
        read = read_config()
        read.start()
        self.__list_hostname = read.get_list_hostname()
        self.__list_username = read.get_list_username()
        self.__list_port = read.get_list_port()
        self.__list_password = read.get_list_password()
        self.__list_master_ip = read.get_list_master_ip()
        self.__list_CPE_credentials = read.get_list_CPE_credentials()
        self.__list_channels = read.get_list_channels()
        self.__err_handler = Error_handler()

    def one_host(self):
        try:
            file_output = open('output.txt', 'a')
            file_output_full = open('output_full.txt','a')
            file_output_full.write('********** START - ONE HOST *******************\n')
            file_output.write('***START - ONE HOST*******************\n')
            file_output.close()
            file_output_full.close()

            for channel in self.__list_channels:
                thread_CPE = CPE_configuration(channel, 'CPE_configuration', self.__list_CPE_credentials[0], self.__list_CPE_credentials[1], self.__list_CPE_credentials[2])
                thread_CPE.start()
                time.sleep(2)
                while (len(threading.enumerate()) !=1):
                    pass


######## DO DOKONCZENIA, TU GDZIES BLAD jest
                if thread_CPE.get_func_state() != 0:
                    result = self.__err_handler.err_search(thread_CPE.get_func_state())
                    if(result == 0):
                        raise Exception('Result - 0, tu bedzie powtorka kodu')
                    else:
                        raise Exception('Brejk de program')

                thread2 = threads_TCP_Upload('log0', "CH%s_TCP_U_%s" % (str(channel), str(self.__list_hostname[0])),
                                             self.__list_hostname[0], self.__list_port[0], self.__list_username[0],
                                             self.__list_password[0], self.__list_master_ip[0])
                thread2.start()
                time.sleep(2)
                while (len(threading.enumerate()) !=1):
                    pass

                if thread2.get_func_state() == -1 or thread2.get_func_state() == -2:
                    raise Exception('Cos nie tak z konfiguracja')

                thread1 = threads_TCP_Download('log0', "CH%s_TCP_D_%s" % (str(channel), str(self.__list_hostname[0])),
                                               self.__list_hostname[0], self.__list_port[0], self.__list_username[0],
                                               self.__list_password[0], self.__list_master_ip[0])
                thread1.start()
                time.sleep(2)
                while (len(threading.enumerate()) != 1):
                    pass

                if thread1.get_func_state() == -1 or thread1.get_func_state() == -2:
                    raise Exception('Cos nie tak z konfiguracja')

                thread4 = threads_UDP_Upload('log0', "CH%s_UDP_U_%s" % (str(channel), str(self.__list_hostname[0])),
                                             self.__list_hostname[0], self.__list_port[0], self.__list_username[0],
                                             self.__list_password[0], self.__list_master_ip[0])
                thread4.start()
                time.sleep(2)
                while (len(threading.enumerate()) != 1):
                    pass

                if thread4.get_func_state() == -1 or thread4.get_func_state() == -2:
                    raise Exception('Cos nie tak z konfiguracja')

                thread3 = threads_UDP_Download('log0', "CH%s_UDP_D_%s" % (str(channel), str(self.__list_hostname[0])),
                                               self.__list_hostname[0], self.__list_port[0], self.__list_username[0],
                                               self.__list_password[0], self.__list_master_ip[0])
                thread3.start()
                time.sleep(2)
                while (len(threading.enumerate()) != 1):
                    pass

                if thread3.get_func_state() == -1 or thread3.get_func_state() == -2:
                    raise Exception('Cos nie tak z konfiguracja')

            file_output = open('output.txt', 'a')
            file_output_full = open('output_full.txt', 'a')
            file_output.write('***END - ONE HOST*********************\n\n\n')
            file_output_full.write('***END - ONE HOST*********************\n\n\n')
            file_output.close()
            file_output_full.close()

        except IOError as IO:
            print(IO)
        except Exception as e:
            print(e)



ob = main()

ob.one_host()

