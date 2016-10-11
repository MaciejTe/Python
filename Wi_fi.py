import time
import threading
import sys

from iperf_threads import *
from Error_handler import ErrorHandler as EH
from configuration import Configuration


class Main(object):

    def __init__(self):
        configuration = Configuration()
        self.conf_data = configuration.conf_data
        self.err_handler = EH()
        self.rep_count = 0

        self.iter_methods = []

    @error_check
    def run_thread(self, thr_desc, channel, wait_switch=True,
                   host_index=0, filename='log0'):

        iperf_threads = IperfThreads()

        threads = {
            'CPE_conf': threading.Thread(
                        target=iperf_threads.cpe_configuration,
                        args=(channel, host_index,
                              'CPE_configuration',
                              self.conf_data)),
            'TCP_upload': threading.Thread(
                            target=iperf_threads.run_thread,
                            args=(filename, host_index,
                                  "CH%s_TCP_U_%s" % (
                                    str(channel),
                                    str(self.conf_data['Hostname']
                                        [host_index])),
                                  self.conf_data,
                                  'TCP_upload')),
            'TCP_download': threading.Thread(
                            target=iperf_threads.run_thread,
                            args=(filename, host_index,
                                  "CH%s_TCP_D_%s" % (
                                    str(channel),
                                    str(self.conf_data['Hostname']
                                        [host_index])),
                                  self.conf_data,
                                  'TCP_download')),
            'UDP_upload': threading.Thread(
                            target=iperf_threads.run_thread,
                            args=(filename, host_index,
                                  "CH%s_UDP_U_%s" % (
                                    str(channel),
                                    str(self.conf_data['Hostname']
                                        [host_index])),
                                  self.conf_data,
                                  'UDP_upload')),
            'UDP_download': threading.Thread(
                            target=iperf_threads.run_thread,
                            args=(filename, host_index,
                                  "CH%s_UDP_D_%s" % (
                                    str(channel),
                                    str(self.conf_data['Hostname']
                                        [host_index])),
                                  self.conf_data,
                                  'UDP_download')),
        }

        if len(self.iter_methods) is 0:
            for key in threads:
                self.iter_methods.append(key)
            self.iter_methods.remove('CPE_conf')
            self.iter_methods.sort()

        try:
            print('wywolanie')
            # thread = threads[thr_desc]
            #
            # thread.start()
            # time.sleep(2)
            # self.wait_for_thread(wait_switch)
        except:
            pass
        finally:
            pass

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

    def error_check(self, run_thread):
        def inner(*args, **kwargs):
            options = {'wait_switch': True,
                       'host_index': 0,
                       'filename': 'log0'}
            options.update(kwargs)
            run_thread(args[0], args[1], options['wait_switch'],
                       options['host_index'], options['filename'])

            if self.rep_count is 0:

                if EH.ERR_ACTION is 0:
                    print('!!!Error!!!:')
                    print(EH.ERR_CODE)
                    print('!!!ACTION!!!: Repeat previous thread.')
                    self.rep_count += 1
                    run_thread(args[0], args[1], options['wait_switch'],
                               options['host_index'], options['filename'])
                elif EH.ERR_ACTION is 1:
                    print('!!!Error!!!:')
                    print(EH.ERR_CODE)
                    print('!!!ACTION!!!: Terminate program.')
                    sys.exit()
        return inner

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
            print(e, 'asd')

            # Obsluga bledow!

    def multiple_hosts(self):
        try:
            self.write_description('START')

            for channel in self.conf_data['Channels']:
                self.run_thread('CPE_conf', channel)
                for method in self.iter_methods:
                    for i in range(3):
                        self.run_thread(method,
                                        channel,
                                        wait_switch=False,
                                        host_index=i)
                    else:
                        self.wait_for_thread()

            self.write_description('END')
        except Exception as e:
            print(e)
            #Obsluga bledow!


ob = Main()
#ob.one_host()
ob.multiple_hosts()