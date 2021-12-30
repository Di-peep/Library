"""
This module creates logger to file
"""
# local imports
import logging
import sys


def create_logger() -> None:
    """
    creates logger to show debug information
    """
    logger = logging.getLogger()
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S', filename='logger.log', filemode='w')

    # to std stream
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)

    # to logger file
    file_handler = logging.FileHandler('logger.log')
    file_handler.setLevel(logging.DEBUG)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
