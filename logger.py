import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'wallet-utility-83', log_file: str = 'app.log') -> logging.Logger:
    """Configures a rotating file logger for the wallet utility."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        # 5MB per file, keep 3 historical backups
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
        
        # Optional: Log to console as well
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger