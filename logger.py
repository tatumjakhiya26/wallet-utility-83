import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name='wallet-utility-83', log_file='wallet.log', level=logging.INFO):
    """Configures a rotating file logger for crypto wallet ops."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Max file size 5MB, keep 3 historical backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5*1024*1024, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Output to console as well
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger

# Instance for global utility access
logger = setup_logger()