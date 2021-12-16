""" Testing the history functions"""
# unit tests
# pylint: disable=duplicate-code
import pytest

from calc.calculator import Calculator
from calc.history.calculations import Calculations

# fixture
@pytest.fixture
def clear_calculator_history_fixture():
    """clears history each time a test is run"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_calc_history()


def test_clear_calculator_history(clear_calculator_history_fixture):
    """ testing the clear history function of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.addition(1, 2) is True
    assert Calculator.addition(2, 5) is True
    assert Calculations.history_calculations_count() == 2
    assert Calculations.clear_calculator_history() is True
    assert Calculations.history_calculations_count() == 0


def test_history_calculations_count(clear_calculator_history_fixture):
    """ testing that the calculator can count the number of calculation results in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.addition(1, 2) is True
    assert Calculator.addition(2, 4) is True
    assert Calculations.history_calculations_count() == 2


def test_last_calculation_result_in_history(clear_calculator_history_fixture):
    """ testing that the calculator can return the last calculation result in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.addition(1, 2) is True
    assert Calculator.addition(2, 4) is True
    assert Calculator.last_calculation_result_in_history() == 6
