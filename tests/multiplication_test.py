""" Testing the multiplication function"""
# unit test
# pylint: disable=duplicate-code

from calc.operations.multiplication import Multiplication

from tests import reading_csv, results_log as log


# multiplication test
def test_calculator_multiply_static():
    """testing that the calculator has a static method for multiplication"""
    # pylint: disable=unused-argument,redefined-outer-name
    path = "done/multiplication.csv"
    table = reading_csv.reading_csv(path)
    for i in range(len(table)):
        # Arrange
        multiplication = Multiplication(table[0][i], (table[1][i]))
        # Act
        # Assert
        assert multiplication.get_result() == table[2][i]
        log.log_components(path, i, "multiplication", multiplication.get_result())
