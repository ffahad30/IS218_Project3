""" Testing the addition function"""

from calc.calculator import Calculator
from calc.history.calculations import Calculations

# addition test
def test_calculator_add_static():
    """testing that the calculator has a static method for addition"""
    Calculations.clear_calculator_history()
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.addition(1, 2) is True
    assert Calculator.addition(2, 5) is True
    assert Calculations.history_calculations_count() == 2
    assert Calculator.last_calculation_result_in_history() == 7
