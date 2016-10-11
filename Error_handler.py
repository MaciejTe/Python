# err_dict = {error_code : ['error description', 0 or 1 - type of action]}
# actions: 0 - try again,repeat part of code; 1 - gtfo&rtfm


class ErrorHandler:

    # Global variables
    ERR_ACTION = None
    ERR_CODE = None

    def __init__(self):

        self.err_dict = {101: ('bad SSH server configuration', 1),
                         102: ('bad pass, bad hostname', 1)
        }

    def err_search(self):
        if self.ERR_CODE in self.err_dict:
            result = self.err_dict[self.ERR_CODE]

            print('!!!ERROR!!!: %s' % result[0])

            self.ERR_ACTION = self.err_dict[self.ERR_CODE]
        else:
            print('There is no such error code!')
            self.ERR_ACTION = 1


def smart_divide(func):
    def inner(*args, **kwargs):
        print(args)
        print("I am going to divide",args[0],"and",args[1]," possible",kwargs['c'])
        if args[1] == 0:
            print("Whoops! cannot divide")
            return

        return func(*args, **kwargs)
    return inner

@smart_divide
def divide(a,b, c=100):
    return a/b

divide(1,2)
