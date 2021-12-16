"""Calculations Class"""

import pandas as pd
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


class Calculations:
    """Manages the history of the calculator"""

    history = []
    calc_history = []
    table = {"value1": [], "value2": [], "operations": [], "result": []}

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
    def clear_calc_history():
        """ clear calc_history list"""
        Calculations.calc_history.clear()

    @staticmethod
    def clear_history_csv():
        """ clear history.csv"""
        Calculations.table["value1"].clear()
        Calculations.table["value2"].clear()
        Calculations.table["operations"].clear()
        Calculations.table["result"].clear()
        Calculations.clear_calc_history()
        Calculations.dataframe = pd.DataFrame(Calculations.table)
        # noinspection PyTypeChecker
        Calculations.dataframe.to_csv("history.csv", index=False)
        return True

    @staticmethod
    def write_history_csv(value1, value2, operation, result):
        """ write history.csv"""
        Calculations.table["value1"].append(value1)
        Calculations.table["value2"].append(value2)
        Calculations.table["operations"].append(operation)
        Calculations.table["result"].append(result)
        Calculations.dataframe = pd.DataFrame(Calculations.table)
        # noinspection PyTypeChecker
        Calculations.dataframe.to_csv("history.csv", index=False)
        return True

    @staticmethod
    def read_history_csv():
        """ read history.csv"""
        dataframe = pd.read_csv("history.csv")
        value1 = dataframe["value1"]
        value2 = dataframe["value2"]
        operations = dataframe["operations"]
        result = dataframe["result"]
        Calculations.clear_calc_history()
        for i in range(len(result)):
            calculation_info = [value1[i], value2[i], operations[i], result[i]]
            Calculations.calc_history.append(calculation_info)
        return True

    @staticmethod
    def return_calc_history():
        """ return calculator history"""
        return Calculations.calc_history

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


