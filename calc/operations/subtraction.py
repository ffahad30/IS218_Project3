"""Subtraction Class"""
from calc.operations.calculation import Calculation


# class
class Subtraction(Calculation):
    """ Subtracting two numbers"""
    # pylint: disable=line-too-long
    def get_result(self):
        """ subtract two numbers and get the result"""
        result = int(self.value_a) - int(self.value_b)
        return result
