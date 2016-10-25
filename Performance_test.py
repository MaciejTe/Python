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
@click.option('--freq', default='24', type=click.Choice(['24', '5']),
              help='Wi-fi frequency choice ; default value=2.4 GHz')
def performance_test(type, udp, time, freq):
    """Method for executing single, multiple and both methods

        Args:
            type (str): type of script operation
            udp (str): udp bandwidth
            time (str): iperf time duration
            freq (str): Wi-fi frequency choice
    """
        udp_validation(udp)
        time_validation(time)

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


def udp_validation(udp):
    """Method validating udp parameter input.

        Args:
            udp (str): UDP bandwidth
    """
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
    """Method validating time parameter input.

        Args:
            time (str): iperf time duration
    """
    try:
        int(time)
        Iperf.DURATION_TIME = time
    except ValueError:
        print('Incorrect value for Iperf time duration')
        sys.exit()


if __name__ == '__main__':
    performance_test()


