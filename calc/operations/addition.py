"""Addition Class"""
from calc.operations.calculation import Calculation


# class
# Subclass #1 in facade pattern
class Addition(Calculation):
    """ Adding two numbers"""
    # pylint: disable=line-too-long
    # get_result is used in the Addition, Subtraction, Multiplication, & Division classes = polymorphism
    def get_result(self):
        """ add two numbers and get the result"""
        # value_a and value_b are seamlessly inherited from calculation class = LSP
        # result is in a namespace
        result = self.value_a + self.value_b
        return result
