""" Testing the addition function"""
# unit test
# pylint: disable=duplicate-code

from calc.operations.addition import Addition

from tests import reading_csv, results_log as log


# addition test
def test_calculator_add_static():
    """testing that the calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    path = "done/addition.csv"
    table = reading_csv.reading_csv(path)
    for i in range(len(table)):
        # Arrange
        addition = Addition(table[0][i], (table[1][i]))
        # Act
        # Assert
        assert addition.get_result() == table[2][i]
        log.log_components(path, i, "addition", addition.get_result())
