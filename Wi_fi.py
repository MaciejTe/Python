import time
import threading
import sys
import datetime
import os

from iperf_threads import *
from Error_handler import ErrorHandler as EH
from configuration import Configuration


def error_check(run_thread):
    def inner(self, *args, **kwargs):
        options = {'wait_switch': True,
                   'host_index': 0,
                   'filename': 'log0'}
        options.update(kwargs)
        run_thread(self, args[0], args[1], wait_switch=options['wait_switch'],
                        host_index=options['host_index'],
                        filename=options['filename'])

        if EH.ERR_ACTION is not None:
            with open('output.txt', 'a') as file_open:
                with open('output_full.txt', 'a') as file_full_open:
                    file_open.write('!!!!!!\n' + EH.ERR_DESC + '\n!!!!!!')
                    file_full_open.write('!!!!!!\n' + EH.ERR_DESC + '\n!!!!!!')

        if EH.ERR_ACTION is 1:
            time.sleep(10)
            print('!!!Error!!!:')
            print(EH.ERR_CODE)
            print('!!!ACTION!!!: Repeat previous thread.')

            run_thread(self, args[0], args[1],
                       options['wait_switch'],
                       options['host_index'],
                       options['filename'])
            if EH.ERR_ACTION is not None:
                print('!!!Error!!!:')
                print(EH.ERR_CODE)
                print('!!!ACTION!!!: Terminate program.')
                sys.exit()

        elif EH.ERR_ACTION is 2:
            print('!!!Error!!!:')
            print(EH.ERR_CODE)
            print('!!!ACTION!!!: Terminate program.')
            sys.exit()
            # 1. stworzyc liste watkow ktore aktualnie zyja
            # 2. posortowac zeby Main byl przedostatni, ostatni watek to ten w ktorym sie obecnie znajdujemy
            # 3. uwalic zgodnie z lista

        EH.ERR_ACTION = None
        EH.ERR_CODE = None

    return inner


class Main(object):

    def __init__(self):
        configuration = Configuration()
        self.conf_data = configuration.conf_data
        self.host_amount = len(self.conf_data['Username'])
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

            thread = threads[thr_desc]

            thread.start()
            
        except RuntimeError:
            EH(2011)
        except Exception as e:
            EH(2012)
            print(e)
        finally:
            self.wait_for_thread(wait_switch)

    def wait_for_thread(self, switch=True):
        try:
            if switch:
                while len(threading.enumerate()) is not 1:
                    pass
        except RuntimeError:
            EH(2021, kill_thread=False)

    def set_date(self):
        curr_datetime = datetime.datetime.today()
        curr_datetime = curr_datetime.strftime('%A, %d. %B %Y %I:%M%p')
        return curr_datetime

    def write_description(self, description, hosts_amount='ONE_HOST'):


        try:

            blank_lines = ('\n', '\n\n\n')
            select_blanklns = 0
            if hosts_amount != 'ONE_HOST':
                select_blanklns = 1

            file_output = open('output.txt', 'a')
            file_output_full = open('output_full.txt', 'a')
            file_output_full.write('*** %s - %s *** %s ***%s'
                                   % (description, hosts_amount,
                                      self.set_date(),
                                      blank_lines[select_blanklns]))
            file_output.write('*** %s - %s *** %s ***%s'
                              % (description, hosts_amount,
                                 self.set_date(),
                                 blank_lines[select_blanklns]))
            file_output.close()
            file_output_full.close()
        except IOError:
            EH(2031, kill_thread=False)
        except Exception as e:
            EH(2032)
            print(e)

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

        except RuntimeError:
            EH(2041)
        except Exception as e:
            print(e)
            EH(2042)

    def multiple_hosts(self):
        try:
            self.write_description('START', 'MULTIPLE_HOSTS')

            for channel in self.conf_data['Channels']:
                self.run_thread('CPE_conf', channel)
                for method in self.iter_methods:
                    for i in range(self.host_amount):
                        filename = ('log%s' % i)
                        self.run_thread(method,
                                        channel,
                                        wait_switch=False,
                                        host_index=i,
                                        filename=filename)
                    else:
                        self.wait_for_thread()
                        os.system('killall iperf')

            self.write_description('END', 'MULTIPLE_HOSTS')

        except RuntimeError:
            EH(2051)
        except Exception as e:
            print(e)
            EH(2052)


