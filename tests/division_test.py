""" Testing the division function"""
# unit test
# pylint: disable=duplicate-code


from calc.operations.division import Division

from tests import reading_csv, results_log as log


# division test
def test_calculator_divide_static():
    """testing that the calculator has a static method for division"""
    # pylint: disable=unused-argument,redefined-outer-name
    path = "done/division.csv"
    table = reading_csv.reading_csv(path)
    for i in range(len(table)):
        # Arrange
        division = Division(table[0][i], (table[1][i]))
        # Act
        # Assert
        assert division.get_result() == table[2][i]
        log.log_components(path, i, "division", division.get_result())
