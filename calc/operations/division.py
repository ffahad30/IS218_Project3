"""Division Class"""
from calc.operations.calculation import Calculation
# pylint: disable=duplicate-code

# class
class Division(Calculation):
    """ Dividing two numbers"""
    # pylint: disable=line-too-long
    def get_result(self):
        """ divide two numbers and get the result"""
        if int(self.value_b) != 0:
            result = int(self.value_a) // int(self.value_b)
        else:
            result = "error"
        return result
