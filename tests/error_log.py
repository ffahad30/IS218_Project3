"""Log file for calculation errors"""

import logging


def log_errors(path, record_number):
    """create log for calculation errors"""
    path = path.split('/')
    file_name = path[len(path) - 1]
    message = file_name + '' + str(record_number)
    logging.error(message)