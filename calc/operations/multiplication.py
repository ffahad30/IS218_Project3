"""Multiplication Class"""
from calc.operations.calculation import Calculation


# class
# Subclass #3 in facade pattern
class Multiplication(Calculation):
    """ Multiplying two numbers"""
    # pylint: disable=line-too-long
    # get_result is used in the Addition, Subtraction, Multiplication, & Division classes = polymorphism
    def get_result(self):
        """ multiply two numbers and get the result"""
        # result is in a namespace
        # value_a and value_b are seamlessly inherited from calculation class = LSP
        result = int(self.value_a) * int(self.value_b)
        return result
