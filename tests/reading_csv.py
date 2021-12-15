"""Reading the CSV files"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long

import shutil
import logging
import pandas as pd


def reading_csv(path):
    """Reading the addition, subtraction, multiplication, division, and division error CSV files"""
    x = pd.read_csv(path)
    # move files to done folder once they are read
    shutil.move(path, "done")
    message = path + ' moved to folder "done" '
    logging.info(message)
    # variables
    value_1 = x['VALUE 1']
    value_2 = x['VALUE 2']
    result = x['RESULT']
    return value_1, value_2, result
