from configobj import ConfigObj


class Configuration(object):
    FILENAME = "conf.ini"

    def __init__(self):
        self.config = ConfigObj(self.FILENAME)
        self.raw_conf_data = dict(self.config)
        self.conf_data = self.change_data_struct()
        if not(self.validation()):
            self.conf_data = None


    def validation(self):
        result = True
        len_list = [len(self.conf_data['Username']),
                    len(self.conf_data['Hostname']),
                    len(self.conf_data['Password']),
                    len(self.conf_data['Port']),
                    ]

        if (sum(len_list) / len(len_list)) is not len_list[0]:
            result = False
        if len(self.conf_data['CPE_credentials']) is not 3:
            result = False
        if len(self.conf_data['Master_IP']) is not 1:
            result = False
        if len(self.conf_data['Channels']) is 0:
            result = False

        return result

    def change_data_struct(self):
        structure = {}
        temp_list = []

        for key in self.raw_conf_data:
            for inner_key in self.raw_conf_data[key]:
                temp_list.append(self.raw_conf_data[key][inner_key])
            structure.update({key: temp_list})
            temp_list = []

        return structure


