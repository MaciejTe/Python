from configobj import ConfigObj


class Configuration(object):
    FILENAME = "conf.ini"

    def __init__(self):
        self.config = ConfigObj(self.FILENAME)
        self.conf_data = dict(self.config)
        if not(self.validation()):
            self.conf_data = None
        print(self.conf_data)


    def validation(self):
        result = True
        len_list = [len(self.conf_data['Username']),
                    len(self.conf_data['Hostname']),
                    len(self.conf_data['Password']),
                    len(self.conf_data['Port']),
                    ]

        if (sum(len_list) / len(len_list)) is not len_list[0]: #co jesli nie
            #  bedzie username, host i paswd??
            result = False
        if(len(self.conf_data['CPE_credentials']) is not 3):
            result = False
        if(len(self.conf_data['Master_IP']) is not 1):
            result = False
        if(len(self.conf_data['Channels']) is 0):
            result = False

        return result




ob = Configuration()
#ob.read_config()
#ob.validation()