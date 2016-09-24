from configobj import ConfigObj

class Configuration(object):
    FILENAME = "conf.ini"

    def __init__(self):
        self.config = ConfigObj(self.FILENAME)
        self.conf_data = {}

    def read_config(self):

        for section in self.config:
            self.conf_data[section] = {}
            for value in self.config[section]:
                #print(value)
                self.conf_data[section].update({value: self.config[section][value]})



        print(self.conf_data)


ob = Configuration()
ob.read_config()
