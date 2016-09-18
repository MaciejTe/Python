import re

############# DODAC METODE DO WYKRESOW !@###############################

class analyze_log():
    
    def get_all_data(self, input_filename, thread_ID):
        try:
            file_output_full = open('output_full.txt', 'a')
            file_input = open(input_filename, 'r')

            file_output_full.write('\n\n****** ' + thread_ID + ' ******\n')
            file_output_full.writelines(file_input)
            file_output_full.close()
            file_input.close()

            return True

        except IOError:
            print('!!!!WARNING!!!! Something went wrong with the input or output file')
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
            if not boolean:
                file_input = open(input_filename,'r')
                for row in file_input:
                    if (row.find('0.0-1',0,100) != -1) or (row.find('0.0- 9',0,100) != -1):
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
        #print("**************************" + row)
        patch_under_100 = r'\d+\W{1}\d+\s+\w+\x2F\D{3}' # ponizej 100Mbits/sec
        patch_above_100 = r'\d+\s+\w+\x2F\D{3}' #powyzej 100 Mbits/sec
        match_under_100 = re.search(patch_under_100,row)
        match_above_100 = re.search(patch_above_100,row)

        if match_under_100 != None:
            result = match_under_100.group()
        elif match_above_100 != None:
            result = match_above_100.group()
        else:
            result = 'Not Found!'
        #print("**************************" + result)
        return result

# ob = analyze_log()
# ob.get_all_data('log0')
# ob.get_mean_value('log0','chuj')
