"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations


@pytest.fixture
def clear_history_fixture():
    """clear calculator's history"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_calculator_history()


# addition test
def test_calculator_add_static(clear_history_fixture):
    """testing that the calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.addition(1, 2) is True
    assert Calculator.addition(2, 5) is True
    assert Calculations.history_calculations_count() == 2
    assert Calculator.last_calculation_result_in_history() == 7


# subtraction test
def test_calculator_subtract_static(clear_history_fixture):
    """testing that the calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.subtraction(9, 6) is True
    assert Calculator.subtraction(10, 5) is True
    assert Calculations.history_calculations_count() == 2
    assert Calculator.last_calculation_result_in_history() == 5


# multiplication test
def test_calculator_multiply_static(clear_history_fixture):
    """testing that the calculator has a static method for multiplication"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.multiplication(4, 5) is True
    assert Calculator.multiplication(2, 4) is True
    assert Calculations.history_calculations_count() == 2
    assert Calculator.last_calculation_result_in_history() == 8

# division test
def test_calculator_divide_static(clear_history_fixture):
    """testing that the calculator has a static method for division"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.division(30, 5) is True
    assert Calculator.division(12, 6) is True
    assert Calculations.history_calculations_count() == 2
    assert Calculator.last_calculation_result_in_history() == 2

# division error test
def test_calculator_divide_error_static(clear_history_fixture):
    """testing that the calculator has a static method for division"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Act
    # Assert
    assert Calculator.division(30, 5) is True
    assert Calculator.division(12, 0) is True
    assert Calculations.history_calculations_count() == 2
    assert Calculator.last_calculation_result_in_history() == "error"

# read_history_csv test
def test_calculator_read_history_csv():
    """testing that the calculator can read history.csv"""
    assert Calculator.read_history_csv() is True

# write_history_csv test
def test_calculator_write_history_csv():
    """testing that the calculator can write to history.csv"""
    Calculator.write_history_csv(3, 6, "addition", 9)
    assert Calculator.write_history_csv(2, 5, "addition", 7) is True

# clear_history_csv test
def test_clear_history_csv():
    """testing that the calculator can clear history.csv"""
    assert Calculator.clear_history_csv() is True

# return_calc_history test
def test_return_calc_history():
    """ testing that the calculator returns a list for history"""
    assert type(Calculator.return_calc_history()) == list
