""" Testing the zero division exception for the division function"""

from calc.calculator import Calculator
from calc.history.calculations import Calculations

# division error test
def test_calculator_divide_error_static():
    """testing that the calculator has a static method for division"""
    Calculations.clear_calculator_history()
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.division(30, 5) is True
    assert Calculator.division(12, 0) is True
    assert Calculations.history_calculations_count() == 2
    assert Calculator.last_calculation_result_in_history() == "error"
