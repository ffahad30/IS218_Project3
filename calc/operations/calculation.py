""" This is the abstract base calculation class"""


# pylint: disable=line-too-long
class Calculation:
    """ calculation class"""

    # pylint: disable=too-few-public-methods
    # default constructor
    # instantiation
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    # class method
    @classmethod
    def create(cls, value_a, value_b):
        """ factory method """
        return cls(value_a, value_b)
