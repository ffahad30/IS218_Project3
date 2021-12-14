"""Division Class"""
from calc.operations.calculation import Calculation
# pylint: disable=duplicate-code

# class
# Subclass #1 in facade pattern
class Division(Calculation):
    """ Dividing two numbers"""

    # pylint: disable=line-too-long
    # get_result is used in the Addition, Subtraction, Multiplication, & Division classes = polymorphism
    def get_result(self):
        """ divide two numbers and get the result"""
        # result is in a namespace
        # value_a and value_b are seamlessly inherited from calculation class = LSP
        if self.value_b != 0:
            result = self.value_a // self.value_b
        else:
            result = "error"
        return result