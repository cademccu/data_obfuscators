


"""
This is meant to function as an interface to create a reader that functios with
the rest of the program.

Readers should function by tokenizing and applying filters.
"""



from abc import ABC, abstractmethod


class Reader(ABC):
    
    def __init__(self):
        pass

    def next_token(self, flags):
        pass

    def stats(self):
        pass
    
