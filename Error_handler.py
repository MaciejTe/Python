# err_dict = {error_code : ['error description', 0 or 1 - type of action]}
# actions: 0 - try again,repeat part of code; 1 - gtfo&rtfm

class Error_handler:
    def __init__(self):
        self.__err_dict = {101 : ('bad SSH server configuration',1),
                           102 : ('bad pass, bad hostname', 1)
        }

    def err_search(self, err_code):
        if(err_code in self.__err_dict):
            result = self.__err_dict[err_code]
            print(result[0])

            if(result[1]  == 0):
                print('Repeat part of code')
            else:
                print('You stupid motherfucker, the end. RTFM')

            return result[1]
        else:
            print('There is no such error code!')
            return 1