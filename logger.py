import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='wallet-utility', log_file='wallet.log'):
    """Initializes a rotating file logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if logger.hasHandlers():
        logger.handlers.clear()

    # Setup rotation: 5MB per file, keep 3 backups
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also log to console for development visibility
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger