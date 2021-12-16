""" This is the increment function"""

from calc.history.calculations import Calculations


# pylint: disable=line-too-long

class Calculator:
    """ This is the Calculator class"""

    # object
    history = []

    # static method
    @staticmethod
    def last_calculation_result_in_history():
        """ return the last result in the calculator's history"""
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    def read_history_csv():
        """ read history.csv"""
        return Calculations.read_history_csv()

    @staticmethod
    def write_history_csv(value1, value2, operation, result):
        """ write history.csv"""
        return Calculations.write_history_csv(value1, value2, operation, result)

    @staticmethod
    def clear_history_csv():
        """ clear history.csv"""
        Calculations.clear_history_csv()
        return True

    @staticmethod
    def return_calc_history():
        """ return calculator history"""
        return Calculations.return_calc_history()

    # static method
    @staticmethod
    def addition(value_a, value_b):
        """ adds two numbers"""
        Calculations.add_addition_result_to_history(value_a, value_b)
        return True

    # static method
    @staticmethod
    def subtraction(value_a, value_b):
        """ subtracts two numbers"""
        Calculations.add_subtraction_result_to_history(value_a, value_b)
        return True

    # static method
    @staticmethod
    def multiplication(value_a, value_b):
        """ multiplies two numbers"""
        Calculations.add_multiplication_result_to_history(value_a, value_b)
        return True

    # static method
    @staticmethod
    def division(value_a, value_b):
        """ divides two numbers"""
        Calculations.add_division_result_to_history(value_a, value_b)
        return True
