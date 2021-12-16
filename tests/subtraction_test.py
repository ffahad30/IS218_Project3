""" Testing the subtraction function"""

from calc.calculator import Calculator
from calc.history.calculations import Calculations

# pylint: disable="consider-using-enumerate"

# subtraction test
def test_calculator_subtract_static():
    """testing that the calculator has a static method for addition"""
    Calculations.clear_calculator_history()
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.subtraction(9, 6) is True
    assert Calculator.subtraction(10, 5) is True
    assert Calculations.history_calculations_count() == 2
    assert Calculator.last_calculation_result_in_history() == 5
