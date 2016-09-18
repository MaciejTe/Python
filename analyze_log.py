import re


class analyze_log():
    
    def get_all_data(self, input_filename, thread_description):
        try:
            file_output = open('output.txt', 'a')
            file_input = open(input_filename, 'r')
            check_var = False

            for row in file_input:
                if row.find('0.0-1', 0, 100) != -1 | row.find('Server Report:', 0, 100) != -1:
                    break

                result = self.__reg_exp_analyze(row)
                print(result)
                if result != 'Not Found!':
                    file_output.write(thread_description + '\t' + result + '\n')
                    check_var = True
            if not check_var:
                raise ValueError('!!!!WARNING!!!! Value not found')

            file_output.close()
            file_input.close()

            return True

        except IOError:
            print('!!!!WARNING!!!! Something went wrong with the input or output file')
            return False
        except ValueError as ve:
            print(ve)
            return False
        except Exception as e:
            print('!!!!WARNING!!!! Something went wrong.\n::::Exception log:\n')
            print(e)
            return False


    def get_mean_value(self,input_filename, thread_description):
        try:
            file_output = open('output.txt', 'a')
            file_input = open(input_filename,'r')

            result = None
            boolean = False
            
            
            for row in file_input:
                if row.find('Server Report',0,100) != -1:
                    boolean = True
                    continue
                if boolean:
                    result = self.__reg_exp_analyze(row)
                    if(result != 'Not Found!'):
                        file_output.write(thread_description +'\t' +result +'\n')
                        break
                    else:
                        raise ValueError('!!!!WARNING!!!! Value not found')
                        break
            if not boolean:
                file_input = open(input_filename,'r')
                for row in file_input:
                    if row.find('0.0-1',0,100) != -1:
                        result = self.__reg_exp_analyze(row)
                        if (result != 'Not Found!'):
                            file_output.write(thread_description +'\t' +result +'\n')
                            break
                        else:
                            raise ValueError('!!!!WARNING!!!! Value not found')
                    
            if (result == None):
                raise ValueError('!!!!WARNING!!!! Row not found')

            file_output.close()
            file_input.close()

            return True

        except IOError:
            print('!!!!WARNING!!!! Something went wrong with the input or output file')
            return False
        except ValueError as ve:
            print(ve)
            return False
        except Exception as e:
            print('!!!!WARNING!!!! Something went wrong.\n::::Exception log:\n')
            print(e)
            return False

    def __reg_exp_analyze(self,row):
        
        patch = r'\d+\W{1}\d+\s+\w+\x2F\D{3}'
        match = re.search(patch,row)
        if match != None:
            result = match.group()
        else:
            result = 'Not Found!'
            
        return result

# from iperf_exec import iperf
#
# ob2 = analyze_log()
#
# ob = iperf('log0','192.168.10.9','lukaspolon', 'fullypein2', 50000, '192.168.10.2')
# ob.TCP_Download()
# ob2.get_mean_value('log0', 'UDP UPLOAD ONE VAL')
# ob.TCP_Upload()
# ob2.get_mean_value('log0', 'UDP UPLOAD ONE VAL')
# ob.UDP_Download()
# ob2.get_mean_value('log0', 'UDP UPLOAD ONE VAL')
# ob.UDP_Upload()
# ob2.get_mean_value('log0', 'UDP UPLOAD ONE VAL')

#ob.get_mean_value('log0', 'UDP UPLOAD ONE VAL')
#ob.get_all_data('thread1.txt', 'UDP UPLOAD')

