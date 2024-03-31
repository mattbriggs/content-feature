import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(log_file='application_log.log', level=logging.INFO):
    """
    Set up the application's logging configuration.
    Logs will be printed to the console and written to a specified log file.

    Parameters:
    - log_file: The path to the log file.
    - level: The logging level, e.g., logging.INFO, logging.DEBUG.
    """
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(level)

    # Format for our loglines
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Setup file handler
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024*5, backupCount=5)
    file_handler.setFormatter(formatter)
    
    # Setup stream (console) handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Add handlers to our logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
