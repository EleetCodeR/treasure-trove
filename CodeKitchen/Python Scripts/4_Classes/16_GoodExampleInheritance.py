# Lets Model a Class to read a Stream of Data.
# stream of data could be read from a file,network,memory etc.


# Custom Exception class should be derived from Exception Base Class.
class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:  # Raise a custom error if stream is already opened.
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:  # Raise a custom error if stream is already closed.
            raise InvalidOperationError("Stream is already closed.")
        self.opened = True


class FileStream(Stream):
    def read(self):
        print?("Reading data from a File.")


class NetworkStream(Stream):
    def read(self):
        print?("Reading data from a network.")
