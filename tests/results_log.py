"""Log file for calculation results"""

import logging


def log_components(path, record_number, operation, calculation_result):
    """create log for calculation results"""
    file_name = path[len(path) - 1]
    message = file_name + '' + str(record_number) + '' + operation + '' + str(calculation_result)
    logging.info(message)