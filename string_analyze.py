import os

class string_analyze:
    def __init__(self,filename):
        self.filename = filename



    def read_file(self):
        #os.system('iperf -c 192.168.10.9 -i 1 | tee %s' % self.filename)

        file = open(self.filename,'r')

        num_lines = self.get_num_lines()

        list_of_rows = []
        count = 0

        while(count<num_lines):
            count += 1

            if(file.next().find('0.0-10.',0,100) != -1):
                list_of_rows.append(count)

        print (len(list_of_rows))
        print (count)


    def get_num_lines(self):
        file = open(self.filename,'r')
        num_lines = sum(1 for line in file)

        return num_lines
