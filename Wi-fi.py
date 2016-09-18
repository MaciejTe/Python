import time
from iperf_threads import *
from read_config import read_config
from Error_handler import Error_handler

class main(object):
    def __init__(self):
        read = read_config()
        read.start()
        #można użyć stałego słownika, ale trzeba doczytać jak :P
        self.__conf_data = {
            'hostname': read.get_list_hostname(),
            'username': read.get_list_username(),
            'port': read.get_list_port(),
            'password': read.get_list_password(),
            'master_ip': read.get_list_master_ip(),
            'CPE_credentials': read.get_list_CPE_credentials(),
            'channels': read.get_list_channels()
        }

        self.__err_handler = Error_handler()

    def __runThread(self, thr_desc, channel,
                    wait_switch=True, host_index=0, filename='log0'):

        threads = {'CPE_conf': CPE_configuration(
                                    channel,
                                    host_index,
                                    'CPE_configuration',
                                    self.__conf_data),
                   'TCP_upload': threads_TCP_Upload(
                                    filename,
                                    host_index,
                                    "CH%s_TCP_U_%s" % (
                                        str(channel),
                                        str(self.__conf_data
                                            ['hostname'][host_index])),
                                    self.__conf_data),
                   'TCP_download': threads_TCP_Download(
                                    filename,
                                    host_index,
                                    "CH%s_TCP_D_%s" % (
                                        str(channel),
                                        str(self.__conf_data
                                            ['hostname'][host_index])),
                                    self.__conf_data),
                   'UDP_upload': threads_UDP_Upload(
                                    filename,
                                    host_index,
                                    "CH%s_UDP_U_%s" % (
                                        str(channel),
                                        str(self.__conf_data
                                            ['hostname'][host_index])),
                                    self.__conf_data),
                   'UDP_download': threads_UDP_Download(
                                    filename,
                                    host_index,
                                    "CH%s_UDP_D_%s" % (
                                        str(channel),
                                        str(self.__conf_data
                                            ['hostname'][host_index])),
                                    self.__conf_data)
                   }

        try:
            thread = threads[thr_desc]
            thread.start()
            time.sleep(2)
            #Dodać obsługę błędów!!!
        except:
            pass
        finally:
            self.__waitForThread(wait_switch)
    
    def __waitForThread(self, switch=True):
        if switch:
            while len(threading.enumerate()) is not 1:
                pass

    def __writeDescription(self, description, hosts_amount='ONE_HOST'):
        try:
            blank_lines = ('\n', '\n\n\n')
            select_blanklns = 0
            if hosts_amount != 'ONE_HOST':
                select_blanklns = 1

            file_output = open('output.txt', 'a')
            file_output_full = open('output_full.txt', 'a')
            file_output_full.write('********** %s - %s *******************%s'
                                   %(description, hosts_amount,
                                     blank_lines[select_blanklns]))
            file_output.write('*** %s - %s *******************%s'
                              % (description, hosts_amount,
                                 blank_lines[select_blanklns]))
            file_output.close()
            file_output_full.close()
        except:
            #Dokończyć obsługę błędów!
            pass

    def one_host(self):
        try:
            self.__writeDescription('START')
            
            for channel in self.__conf_data['channels']:

                self.__runThread('CPE_conf', channel)
                self.__runThread('TCP_upload', channel)
                self.__runThread('TCP_download', channel)
                self.__runThread('UDP_upload', channel)
                self.__runThread('UDP_download', channel)

            self.__writeDescription('END')


        except:
            #Obsługa błędów!!!!
            pass




ob = main()

ob.one_host()

