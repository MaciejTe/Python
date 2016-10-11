from Wi_fi import Main
import click
from iperf_exec import Iperf


@click.command()
@click.option('--type', type=click.Choice(['single', 'multiple', 'both']))
@click.option('--udp', default='100M', help='UDP bandwidth for iperf; Usage: 10M, 100M, 500M, man iperf')
def performance_test(type, udp):
        Iperf.UDP_BANDWIDTH = udp
        if type == 'single':
            single = Main()
            single.one_host()
        elif type == 'multiple':
            click.echo('Multiple hosts')
            click.echo(Iperf.UDP_BANDWIDTH)
            #TODO
        elif type == 'both':
            click.echo('Both methods')
            click.echo(udp)


if __name__ == '__main__':
    performance_test()

