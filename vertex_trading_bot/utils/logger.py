"""
Logger Module
"""

import logging
from datetime import datetime


def setup_logger(name, log_file, level=logging.INFO):
    """Function to set up a logger"""
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# Create loggers
trade_logger = setup_logger("trade_log", "logs/trades.log")
error_logger = setup_logger("error_log", "logs/errors.log", level=logging.ERROR)


def log_trade(action, amount, price):
    """Function to log trade actions"""
    trade_logger.info(f"{action}: Amount: {amount}, Price: {price}")


def log_error(error_message):
    """Function to log errors"""
    error_logger.error(error_message)
