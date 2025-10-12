import contextlib


@contextlib.contextmanager
def file_open():
    print('Opening file')
    yield
    print('Closing file')


with file_open():
    print('Inside with block')


class Sample:
    def __enter__(self):
        print('Opening file')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Closing file')

    def do_something(self):
        print('Doing something')


with Sample() as s:
    s.do_something()
