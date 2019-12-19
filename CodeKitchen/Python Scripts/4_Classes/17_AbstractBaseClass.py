# code taken from last ex.
from abc import ABC, abstractmethod

# abc is modules name abstract base class, ABC is a class, abstractmethod is a method to be used as a decorator.


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
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

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a File.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")


# stream = Stream()
# stream.open()

# NOTE: PROBLEM-1:
# The problem here is that Stream is an Abstract concept and we shouldn't be able to call open method on it.
# hence we should not be able to create instance of this class instead we should always derive subclass from it and
# create instance of the subclass.
# As we only created Baseclass to use a common code across all streams.

# NOTE: PROBLEM-2:
# Currently there is no way to enforce a common interface across all kinds of streams.
# (eg. Both streams have 'read' method, so we MUST REMEMBER to keep is same for any new stream to maintain consistency.)

# How to Solve these Problems?
# - Abstract Base Class. (make Stream class Abstract Base-Class by deriving from ABC class)
# - define a common interface for all streams.(using decorator @abstractmethod)
# - stream = Stream()  => this will show redline: Abstract class 'Stream' with abstract methods instantiated
# and throw error : TypeError: Can't instantiate abstract class Stream with abstract methods read
# it is because when a class has Abstract method, the class becomes Abstract Class and we can not instantiate abstract class.

class MemoryStream(Stream):
    # pass
    def read(self):
        print('Reading data from MemoryStream.')


# NOTE:
    # any class derived from abstract class ('Stream') has to implement abstractmethod ('read'); otherwise that class also become abstract.
    # hence to instantiate MemoryStream (i.e, to Convert it into a CONCRETE CLASS), define read method.

stream = MemoryStream()
stream.open()
