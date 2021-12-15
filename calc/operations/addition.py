"""Addition Class"""
from calc.operations.calculation import Calculation


# class
class Addition(Calculation):
    """ Adding two numbers"""
    # pylint: disable=line-too-long
    def get_result(self):
        """ add two numbers and get the result"""
        result = int(self.value_a) + int(self.value_b)
        return result
