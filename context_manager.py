import contextlib
import sys


class LoggingContextManager:
    def __enter__(self):
        print("LoggingContextManager.__enter__()")
        return "You are in a with-block"

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print(f"LoggingContextManager.__exit__", "normal exit detected")
        else:
            print(f"LoggingContextManager.__exit__({exc_type}, {exc_value}, {exc_tb})")
        return True


# with LoggingContextManager() as x:
#     print(x)

# with LoggingContextManager() as x:
#     raise ValueError("Something has gone wrong")

# try:
#     with LoggingContextManager() as x:
#         raise ValueError("Something has gone wrong")
# except ValueError:
#     print("*** ValueError detected ***")

@contextlib.contextmanager
def logging_context_manager():
    print("logging_context_manager: enter")
    try:
        yield "You are in a with-block"
        print("logging_context_manager: normal exit")
    except Exception:
        print("logging_context_manager: exceptional exit", sys.exc_info())
        raise


# with logging_context_manager() as x:
#     print(x)

# with logging_context_manager() as x:
#     raise ValueError('Something has gone wrong')


@contextlib.contextmanager
def nest_test(name):
    print('Entering', name)
    yield name
    print('Exiting', name)


# with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
#     print('Body')

@contextlib.contextmanager
def propagator(name, propagate):
    try:
        yield
        print(name, 'excited normally')
    except Exception:
        print(name, 'received an exception')
        if propagate:
            raise


with propagator('outer', True), propagator('inner', True):
    raise TypeError('Cannot convert lead into gold')

# f = open('readme.md', 'r')
# with f as g:
#     print(f is g)