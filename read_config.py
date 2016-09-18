class read_config():
    def __init__(self):
        self.__list_hostname = []
        self.__list_port = []
        self.__list_username = []
        self.__list_password = []
        self.__list_master_ip = []
        self.__list_channels = []
        self.__list_CPE_credentials = []
        self.__setup_filename = 'configuration.txt'

    def start(self):

        self.__check_var = self.__read_conf_data()
        #self.__print_config_content()
        return self.__check_var

    def __read_conf_data(self):
        try:

            file = open(self.__setup_filename, 'r')
            line = file.readline()

            line = self.__analyze_block('@hostname','@port@',file,line,self.__list_hostname)
            line = self.__analyze_block('@port@', '@username@',file,line,self.__list_port)
            line = self.__analyze_block('@username@', '@password@',file,line,self.__list_username)
            line = self.__analyze_block('@password@', '@master_ip@',file,line,self.__list_password)
            line = self.__analyze_block('@master_ip@', '@CPE_credentials@',file,line,self.__list_master_ip)
            line = self.__analyze_block('@CPE_credentials@', '@channels@',file,line,self.__list_CPE_credentials)
            line = self.__analyze_block('@channels@', '@end@',file,line,self.__list_channels)

            file.close()
            debug_var = self.__check_content()
            return debug_var

        except IOError:
            print('!!!!WARNING!!!! Something went wrong with the config file')
            return False
        except Exception as e:
            print('!!!!WARNING!!!! Something went wrong.\n::::Exception log:\n')
            print(e)
            return False


    def __analyze_block(self,start,end,file,line,output_list):

        if (line.find(start, 0, 100) != -1):
            nline = file.readline()

        while (nline.find(end, 0, 100) == -1):
            stripped_line = nline.rstrip('\n')
            stripped_line = stripped_line.strip()
            if (stripped_line != ''):
                output_list.append(stripped_line)
            nline = file.readline()

        return nline

    def __print_config_content(self):

        def pr(list_name):
            for x in list_name:
                if (x != None):
                    print("...%s" % x)
                else:
                    print('NONE!!!')
        print("Hostname:")
        pr(self.__list_hostname)
        print("Port:")
        pr(self.__list_port)
        print("Username:")
        pr(self.__list_username)
        print("Password:")
        pr(self.__list_password)
        print("Master_ip:")
        pr(self.__list_master_ip)
        print("CPE_credentials:")
        pr(self.__list_CPE_credentials)
        print("Channels:")
        pr(self.__list_channels)



    def __check_content(self):
        try:
            hn_len = len(self.__list_hostname)
            un_len = len(self.__list_username)
            p_len = len(self.__list_port)
            pass_len = len(self.__list_password)
            master_len = len(self.__list_master_ip)

            if all( 0 == x for x in(hn_len, un_len, p_len, pass_len, master_len)):
                raise ValueError('!!!!WARNING!!!! One of the config blocks is empty')

            if all(hn_len != x for x in (un_len, p_len, pass_len)):
                raise ValueError('!!!!WARNING!!!! Config file is not correct:\n::::Numbers of variables in lists are not match')

            print('::::Config file is correct')
            return True

        except ValueError as VE:
            print(VE)
            return False
        except Exception as e:
            print('!!!!WARNING!!!! Something went wrong.\n::::Exception log::::\n')
            print(e)
            return False



    def get_list_hostname(self):
        return self.__list_hostname

    def get_list_port(self):
        return self.__list_port

    def get_list_username(self):
        return self.__list_username

    def get_list_password(self):
        return self.__list_password

    def get_list_master_ip(self):
        return self.__list_master_ip
    
    def get_list_CPE_credentials(self):
        return self.__list_CPE_credentials

    def get_list_channels(self):
        return self.__list_channels

#ob = read_config()
#ob.start()


