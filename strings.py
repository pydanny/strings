__author__ = 'Daniel Greenfeld'
__version__ = "0.1.0"


class string(str):
    """ Python strings for humans """

    def len(self):
        return self.__len__()

    @property
    def length(self):
        return self.len()

    @property
    def size(self):
        return self.length
        
    def add(self, value):
        return self + string(value)
        
    def __add__(self, value):
        raise NotImplementedError("Use add instead")

if __name__ == "__main__":
    s = string("Hello")
    x = s.add(", world")
    print type(x)
    