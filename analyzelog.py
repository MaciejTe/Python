import re
from Error_handler import ErrorHandler as EH

class AnalyzeLog(object):
    """Class for analyze iperf log"""

    FILE_FULL = 'output_full.txt'
    FILE_OUTPUT = 'output.txt'

    def get_all_data(self, input_filename, thread_id):

        try:
            file_output_full = open(self.FILE_FULL, 'a')
            file_input = open(input_filename, 'r')

            file_output_full.write('\n\n****** ' + thread_id + ' ******\n')
            file_output_full.writelines(file_input)
            file_output_full.close()
            file_input.close()

            return True

        except IOError:
            EH(3011)
            return False
        except Exception as e:
            EH(3012)
            print(e)
            return False

    def get_mean_value(self, input_filename, thread_description):
        try:
            file_output = open(self.FILE_OUTPUT, 'a')
            file_input = open(input_filename, 'r')

            result = None
            boolean = False

            for row in file_input:
                if row.find('Server Report', 0, 100) != -1:
                    boolean = True
                    continue
                if boolean:
                    result = self.__reg_exp_analyze(row)

                    if result != 'Not Found!':
                        file_output.write(thread_description
                                          + '\t' + result + '\n')
                        break
                    else:
                        raise ValueError('!!!!WARNING!!!! Value not found')
            if not boolean:
                file_input = open(input_filename,'r')
                for row in file_input:
                    if (row.find('0.0-1', 0, 100) != -1) or \
                       (row.find('0.0- 9', 0, 100) != -1):
                        result = self.__reg_exp_analyze(row)

                        if result != 'Not Found!':
                            file_output.write(thread_description
                                              + '\t ' + result + '\n')
                            break
                        else:
                            raise ValueError('!!!!WARNING!!!! Value not found')

            if result is None:
                raise ValueError('!!!!WARNING!!!! Row not found')

            file_output.close()
            file_input.close()

            return True

        except IOError:
            EH(3021)
            return False
        except ValueError as ve:
            EH(3022)
            return False
        except Exception as e:
            EH(3023)
            print(e)
            return False

    def __reg_exp_analyze(self, row):

        # ponizej 100Mbits/sec
        patch_under_100 = r'\d+\W{1}\d+\s+\w+\x2F\D{3}'
        # powyzej 100 Mbits/sec
        patch_above_100 = r'\d+\s+\w+\x2F\D{3}'
        match_under_100 = re.search(patch_under_100, row)
        match_above_100 = re.search(patch_above_100, row)

        if match_under_100 is not None:
            result = match_under_100.group()
        elif match_above_100 is not None:
            result = match_above_100.group()
        else:
            result = 'Not Found!'

        return result
