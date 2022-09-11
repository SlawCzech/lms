

class LoggingContextManager:
    def __enter__(self): # co się wykona PRZED
        print('Enter')
        return "You are in a with-block"

    def __exit__(self, exc_type, exc_val, exc_tb): # co się wykona PO wyjściu
        if exc_type is None:
            print('Exit, normal exit detected')
        else:
            print('Exit, exception detected', exc_type, exc_val, exc_tb)


with LoggingContextManager() as x:
    print(x)
    raise ValueError('hehehe')

