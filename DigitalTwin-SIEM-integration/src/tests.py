"""
FP tests.py
"""

from utils import fp_logger


def test_fp_logger():

    fp_logger.debug("TEST: debug message")
    fp_logger.info("TEST: info message")
    fp_logger.warning("TEST: warning message")
    fp_logger.error("TEST: error message")
    fp_logger.critical("TEST: critical message")
