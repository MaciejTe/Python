from iperf_exec import Iperf
from analyzelog import AnalyzeLog
from SshConnection import SshConnection


class IperfThreads:
    """Thread bodies implementation"""

    def cpe_configuration(self, channel, host_index, thread_id, conf_data):
        """Method for cpe configuration thread

            Args:
                channel (str): router channel
                host_index (int): conf_data index
                thread_id (str): thread description
                conf_data (dict): data from configuration

        """
        ssh_conn = SshConnection(conf_data, host_index)

        print("Starting " + thread_id)
        ssh_conn.connect_to_cpe(channel, SshConnection.WIFI_FREQ)

    def run_thread(self, filename, host_index, thread_id,
                   conf_data, iperf_choice):
        """Method for TCP_upload, TCP_download,
            UDP_upload and UDP_download threads

            Args:
                filename (str): temporary file
                host_index (int): conf_data index
                thread_id (str): thread description
                conf_data (dict): data from configuration

        """

        iperf = Iperf(filename, conf_data, host_index)

        print("Starting " + thread_id)

        if iperf_choice == 'TCP_upload':
            iperf.tcp_upload()
        elif iperf_choice == 'TCP_download':
            iperf.tcp_download()
        elif iperf_choice == 'UDP_upload':
            iperf.udp_upload()
        elif iperf_choice == 'UDP_download':
            iperf.udp_download()

        ob = AnalyzeLog()
        ob.get_mean_value(filename, thread_id)
        ob.get_all_data(filename, thread_id)

