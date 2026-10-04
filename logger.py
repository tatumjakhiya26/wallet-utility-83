import logging
import sys
from logging.handlers import RotatingFileHandler

def get_wallet_logger(name: str) -> logging.Logger:
    """
    Initializes a standardized logger for wallet-utility-83 components.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Console output for real-time monitoring
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Rotating file output for persistent debug tracking
        file_handler = RotatingFileHandler(
            'wallet_utility.log', 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# Instantiate shared logger instance for application
app_logger = get_wallet_logger('wallet-utility-83')