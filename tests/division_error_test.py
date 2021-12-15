""" Testing the division function's ZeroDivisionError exception"""
# unit test
# pylint: disable=duplicate-code


from calc.operations.division import Division

from tests import reading_csv, error_log as log


# division error test
def test_calculator_divide_error_static():
    """testing that the calculator throws an exception for the ZeroDivisionError"""
    # pylint: disable=unused-argument,redefined-outer-name
    path = "done/divisionerror.csv"
    table = reading_csv.reading_csv(path)
    for i in range(len(table)):
        # Arrange
        division = Division(table[0][i], (table[1][i]))
        # Act
        # Assert
        assert division.get_result() == table[2][i]
        log.log_errors(path, i)
