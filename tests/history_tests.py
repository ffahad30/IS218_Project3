""" Testing the history functions"""
# unit tests
# pylint: disable=duplicate-code
import pytest

from calc.calculator import Calculator


# Arrange step for each of the unit tests
# fixture
@pytest.fixture
def clear_calculator_history_fixture():
    """clears history each time a test is run"""
    # pylint: disable=redefined-outer-name
    Calculator.clear_calculator_history()


def test_clear_calculator_history(clear_calculator_history_fixture):
    """ testing the clear history function of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 5) == 7
    assert Calculator.history_calculations_count() == 2
    assert Calculator.clear_calculator_history() is True
    assert Calculator.history_calculations_count() == 0


def test_history_calculations_count(clear_calculator_history_fixture):
    """ testing that the calculator can count the number of calculation logs in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 4) == 6
    assert Calculator.history_calculations_count() == 2


def test_first_calculation_result_in_history(clear_calculator_history_fixture):
    """ testing that the calculator can return the first calculation result in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 4) == 6
    assert Calculator.first_calculation_result_in_history() == 3


def test_last_calculation_result_in_history(clear_calculator_history_fixture):
    """ testing that the calculator can return the last calculation result in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.add_numbers(1, 2) == 3
    assert Calculator.add_numbers(2, 4) == 6
    assert Calculator.last_calculation_result_in_history() == 6