import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'wallet-utility-83', log_file: str = 'app.log', level: int = logging.INFO):
    """Configures a rotating file logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        # 5MB log rotation with 3 backup files
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Optional: log to console as well
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Initialize default logger instance
logger = setup_logger()