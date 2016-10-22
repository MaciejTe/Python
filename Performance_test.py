import click
import re
import sys
from iperf_exec import Iperf
from Wi_fi import Main
from SshConnection import SshConnection as SSH


@click.command()
@click.option('--type', type=click.Choice(['single', 'multiple', 'both']),
              help='Type of operation')
@click.option('--udp', default='100M',
              help='UDP bandwidth for iperf; Usage: 10M, 100M, 500M, man iperf')
@click.option('--time', default='10', help='Time duration for each Iperf call')
@click.option('--freq', default='24', help='Wi-fi frequency choice ; '
                                           'default value=2.4 GHz')
def performance_test(type, udp, time, freq):
        udp_validation(udp)
        time_validation(time)
        freq_validation(freq)

        if type == 'single':
            single = Main()
            single.one_host()
        elif type == 'multiple':
            multiple = Main()
            multiple.multiple_hosts()
            #TODO
        elif type == 'both':
            single = Main()
            multiple = Main()
            single.one_host()
            multiple.multiple_hosts()
            #PRZETESTOWAC!

def udp_validation(udp):
    patch1 = r'\d+\x4D'
    patch2 = r'\d+'
    match1 = re.search(patch1, udp)
    match2 = re.search(patch2, udp)
    if match1 is not None:
        Iperf.UDP_BANDWIDTH = match1.group()
    elif match2 is not None:
        Iperf.UDP_BANDWIDTH = match2.group()
    else:
        print('UDP bandwidth has to be entered in proper form')
        sys.exit()

def time_validation(time):
    try:
        int(time)
        Iperf.DURATION_TIME = time
    except ValueError:
        print('Incorrect value for Iperf time duration')
        sys.exit()

def freq_validation(freq):
    try:
        if freq == '2.4':
            SSH.WIFI_FREQ = '24'
        elif freq == '5':
            SSH.WIFI_FREQ = '5'
    except ValueError:
        print('Incorrect value for Wi-fi frequency ; 24 or \'5\' values \n'
              'are accepted ')
        sys.exit()



if __name__ == '__main__':
    performance_test()

#TODO
#help
#
