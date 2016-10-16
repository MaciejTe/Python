from configobj import ConfigObj
from Error_handler import ErrorHandler as EH

class Configuration(object):
    FILENAME = "conf.ini"

    def __init__(self):
        self.config = ConfigObj(self.FILENAME)
        self.raw_conf_data = dict(self.config)
        self.conf_data = self.change_data_struct()
        if not(self.validation()):
            self.conf_data = None

    def validation(self):
        # sprawdzic czy plik istnieje i nie jest pusty | modul OS - isfile
        result = True
        len_list = [len(self.conf_data['Username']),
                    len(self.conf_data['Hostname']),
                    len(self.conf_data['Password']),
                    len(self.conf_data['Port']),
                    ]
        try:
            if (sum(len_list) / len(len_list)) is not len_list[0]:
                result = False
                raise ValueError
            if len(self.conf_data['CPE_credentials']) is not 3:
                result = False
                raise ValueError
            if len(self.conf_data['Master_IP']) is not 1:
                result = False
                raise ValueError
            if len(self.conf_data['Channels']) is 0:
                result = False
                raise ValueError
        except ValueError:
            EH(4011)
        except Exception as e:
            EH(4012)
            print(e)

        return result

    def change_data_struct(self):
        structure = {}
        temp_list = []
        try:
            for key in self.raw_conf_data:
                for inner_key in self.raw_conf_data[key]:
                    temp_list.append(self.raw_conf_data[key][inner_key])
                structure.update({key: temp_list})
                temp_list = []
            return structure
        except LookupError:
            EH(4021, kill_thread=False)



