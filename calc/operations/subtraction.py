"""Subtraction Class"""
from calc.operations.calculation import Calculation


# class
# Subclass #2 in facade pattern
class Subtraction(Calculation):
    """ Subtracting two numbers"""
    # pylint: disable=line-too-long
    # get_result is used in the Addition, Subtraction, Multiplication, & Division classes = polymorphism
    def get_result(self):
        """ subtract two numbers and get the result"""
        # result is in a namespace
        # value_a and value_b are seamlessly inherited from calculation class = LSP
        result = int(self.value_a) - int(self.value_b)
        return result
