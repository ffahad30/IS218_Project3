""" This is the increment function"""

from calc.history.calculations import Calculations


# pylint: disable=line-too-long

# all of the calculator's methods and variables are in class Calculator = encapsulation
# static class
# main class in facade pattern which inherits Addition, Subtraction, Multiplication, and Subtraction classes
# calculator class and all of its functions only have the methods and properties needed, nothing extra = ISP
# all functions are open for extension but closed for modification ; they cannot be changed = OCP
# separate functions for each of the calculator's math and history operations = SRP
class Calculator:
    """ This is the Calculator class"""

    # object
    history = []

    # static method
    @staticmethod
    def last_calculation_result_in_history():
        """ return the last result in the calculator's history"""
        return Calculations.get_last_calculation_result_value()

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
