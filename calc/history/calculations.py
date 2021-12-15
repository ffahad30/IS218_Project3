"""Calculations Class"""

from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


class Calculations:
    """Manages the history of the calculator"""

    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_calculator_history():
        """clear the calculator's history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def history_calculations_count():
        """count the number of calculation results in the history"""
        return len(Calculations.history)

    @staticmethod
    def last_calculation_result_in_history():
        """return the last result in the calculator's history"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """get the result of the last calculation"""
        calculation = Calculations.last_calculation_result_in_history()
        return calculation.get_result()

    @staticmethod
    def first_calculation_result_in_history():
        """return the first result in the calculator's history"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """add calculation result to the history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition_result_to_history(value_a, value_b):
        """adding and appending result to history"""
        Calculations.add_calculation(Addition.create(value_a, value_b))
        return True

    @staticmethod
    def add_subtraction_result_to_history(value_a, value_b):
        """subtracting and appending result to history"""
        Calculations.add_calculation(Subtraction.create(value_a, value_b))
        return True

    @staticmethod
    def add_multiplication_result_to_history(value_a, value_b):
        """multiplying and appending result to history"""
        Calculations.add_calculation(Multiplication.create(value_a, value_b))
        return True

    @staticmethod
    def add_division_result_to_history(value_a, value_b):
        """dividing and appending result to history"""
        Calculations.add_calculation(Division.create(value_a, value_b))
        return True

