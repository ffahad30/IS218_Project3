""" Testing the multiplication function"""

from calc.calculator import Calculator
from calc.history.calculations import Calculations

# multiplication test
def test_calculator_multiply_static():
    """testing that the calculator has a static method for multiplication"""
    Calculations.clear_calculator_history()
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.multiplication(4, 5) is True
    assert Calculator.multiplication(2, 4) is True
    assert Calculations.history_calculations_count() == 2
    assert Calculator.last_calculation_result_in_history() == 8
