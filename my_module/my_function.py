# my_module/my_function.py

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

class MyImmutableClass:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value

class MyMutableClass:
    def __init__(self):
        self._data = []
    
    def add_item(self, item):
        self._data.append(item)
    
    def get_items(self):
        return self._data

class MyBaseClass:
    def __init__(self):
        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

class MyDerivedClass(MyBaseClass):
    def __init__(self):
        super().__init__()
