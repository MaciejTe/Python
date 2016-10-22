# err_dict = {error_code : ['error description', 0 or 1 - type of action]}
# actions: 1 - try again,repeat part of code; 2 - gtfo&rtfm


# first 2 digits - class
# third digit - method
# fourth digit - error

import sys


class ErrorHandler:

    # Global variables
    ERR_ACTION = None

    def __init__(self, err_code, kill_thread=True):

        self.kill_thread = kill_thread
        self.err_dict = {
                         1011: ('Exception: BadAuthenticationType,\n'
                                'Class: SshConnection, '
                                'Method: connect_to_host.', 2),
                         1012: ('Exception: AuthenticationException,\n'
                                'Class: SshConnection'
                                'Method: connect_to_host', 2),
                         1013: ('Exception: unknown,\n '
                                'Class: SshConnection '
                                'Method: connect_to_host.', 1),
                         1021: ('Exception: AuthenticationException,\n '
                                'Class: SshConnection'
                                'Method: connect_to_cpe.', 2),
                         1022: ('Exception: unknown,\n '
                                'Class: SshConnection'
                                'Method: connect_to_cpe', 1),
                         2011: ('Exception: RuntimeError,\n '
                                'Class: Main'
                                'Method: run_thread', 1),
                         2012: ('Exception: unknown,\n '
                                'Class: Main'
                                'Method: run_thread', 1),
                         2021: ('Exception: RuntimeError,\n '
                                'Class: Main'
                                'Method: write_description', 1),
                         2031: ('Exception: IOError,\n '
                                'Class: Main'
                                'Method: write_description', 1),
                         2032: ('Exception: unknown,\n '
                                'Class: Main'
                                'Method: write_description', 1),
                         2041: ('Exception: RuntimeError,\n '
                                'Class: Main'
                                'Method: one_host', 2),
                         2042: ('Exception: unknown,\n '
                                'Class: Main'
                                'Method: one_host', 2),
                         2051: ('Exception: RuntimeError,\n '
                                'Class: Main'
                                'Method: multiple_hosts', 2),
                         2052: ('Exception: unknown,\n '
                                'Class: Main'
                                'Method: multiple_hosts', 2),
                         3011: ('Exception: IOError,\n '
                                'Class: AnalyzeLog'
                                'Method: get_all_data', 1),
                         3012: ('Exception: unknown,\n '
                                'Class: AnalyzeLog'
                                'Method: get_all_data', 1),
                         3021: ('Exception: IOError,\n '
                                'Class: AnalyzeLog'
                                'Method: get_mean_value', 1),
                         3022: ('Exception: ValueError,\n '
                                'Class: AnalyzeLog'
                                'Method: get_mean_value', 1),
                         3023: ('Exception: ValueError,\n '
                                'Class: AnalyzeLog'
                                'Method: get_mean_value', 2),
                         4011: ('Exception: ValueError,\n '
                                'Class: Configuration'
                                'Method: validation', 2),
                         4012: ('Exception: ValueError,\n '
                                'Class: Configuration'
                                'Method: validation', 2),
                         4021: ('Exception: LookupError,\n '
                                'Class: Configuration'
                                'Method: change_data_struct', 2),


        }

        self.err_search(err_code)


    def err_search(self, err_code):

        if err_code in self.err_dict:
            result = self.err_dict[err_code]

            print('!!!ERROR %s !!!: %s' % (err_code, result[0]))
            ErrorHandler.ERR_ACTION = result[1]
        else:
            print('There is no such error code!')
            ErrorHandler.ERR_ACTION = 2

        if self.kill_thread:
            sys.exit()
            
            
            