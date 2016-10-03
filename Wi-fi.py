import time

from iperf_threads import *
from read_config import read_config
from Error_handler import Error_handler
from configuration import Configuration

class Main(object):

    def __init__(self):
        # read = read_config()
        # read.start()
        configuration = Configuration()
        self.conf_data = configuration.conf_data
        self.__err_handler = Error_handler()

    def run_thread(self, thr_desc, channel, wait_switch=True,
                   host_index=0, filename='log0'):

        threads = {
            'CPE_conf': CPE_configuration(
                channel,
                host_index,
                'CPE_configuration',
                self.conf_data),
            'TCP_upload': threads_TCP_Upload(
                filename,
                host_index,
                "CH%s_TCP_U_%s" % (
                    str(channel),
                    str(self.conf_data['Hostname'][host_index])),
                        self.conf_data),
            'TCP_download': threads_TCP_Download(
                filename,
                host_index,
                "CH%s_TCP_D_%s" % (
                    str(channel),
                    str(self.conf_data['Hostname'][host_index])),
                        self.conf_data),
            'UDP_upload': threads_UDP_Upload(
                filename,
                host_index,
                "CH%s_UDP_U_%s" % (
                    str(channel),
                    str(self.conf_data['Hostname'][host_index])),
                        self.conf_data),
            'UDP_download': threads_UDP_Download(
                filename,
                host_index,
                "CH%s_UDP_D_%s" % (
                    str(channel),
                    str(self.conf_data['Hostname'][host_index])),
                        self.conf_data)
        }

        try:
            thread = threads[thr_desc]
            thread.start()
            time.sleep(2)
            # Dodac obsluge bledow!!!
        except:
            pass
        finally:
            self.wait_for_thread(wait_switch)

    def wait_for_thread(self, switch=True):
        if switch:
            while len(threading.enumerate()) is not 1:
                pass

    def write_description(self, description, hosts_amount='ONE_HOST'):
        try:
            blank_lines = ('\n', '\n\n\n')
            select_blanklns = 0
            if hosts_amount != 'ONE_HOST':
                select_blanklns = 1

            file_output = open('output.txt', 'a')
            file_output_full = open('output_full.txt', 'a')
            file_output_full.write('********** %s - %s *******************%s'
                                   % (description, hosts_amount,
                                      blank_lines[select_blanklns]))
            file_output.write('*** %s - %s *******************%s'
                              % (description, hosts_amount,
                                 blank_lines[select_blanklns]))
            file_output.close()
            file_output_full.close()
        except:
            # Dokonczyc obsluge bledow!!
            pass

    def one_host(self):
        try:
            self.write_description('START')

            for channel in self.conf_data['Channels']:
                self.run_thread('CPE_conf', channel)
                self.run_thread('TCP_upload', channel)
                self.run_thread('TCP_download', channel)
                self.run_thread('UDP_upload', channel)
                self.run_thread('UDP_download', channel)

            self.write_description('END')


        except Exception as e:
            print(e,'asd')

            # Obsluga bledow!
            pass


ob = Main()
ob.one_host()

#
# if(args_len == 1):
#     print('Application takes exactly one argument: -s or -m')
#     print('-h or --help --> Help')
# elif(sys.argv[1] == '-s'):
#     ob.single_host()
# elif(sys.argv[1] == '-m'):
#     ob.multiple_hosts()
# elif(sys.argv[1] == '-h' or sys.argv[1] == '--help'):
#     print('Usage:\n -s --> single host performance test')
#     print('-m --> multiple(3) hosts performance test')
