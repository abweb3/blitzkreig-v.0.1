"""
Logger Module
"""

import logging
import os


def setup_logger(name, log_file, level=logging.INFO):
    """Function to set up a logger; ensure directory exists."""
    # Ensure the directory for the log file exists
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)  # Create the log directory if it doesn't exist

    # Create a formatter that specifies the format of log messages
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Create a file handler that logs even debug messages
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    # Create a logger with the specified name and level
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# Setup loggers for both trade and error logs
trade_logger = setup_logger("trade_logger", "logs/trade.log", logging.INFO)
error_logger = setup_logger("error_logger", "logs/error.log", logging.ERROR)


def log_trade(action, amount, price):
    """Function to log trade actions. Uses old-style % formatting to delay string interpolation."""
    trade_logger.info("Action: %s, Amount: %s, Price: %s", action, amount, price)


def log_error(error_message):
    """Function to log errors. Uses old-style % formatting for efficiency."""
    error_logger.error("Error: %s", error_message)


# Example usage of the logging functions
if __name__ == "__main__":
    log_trade("BUY", 100, 50.5)
    log_error("Connection timeout occurred")
