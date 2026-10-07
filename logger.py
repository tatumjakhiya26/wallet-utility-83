import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = "wallet.log") -> logging.Logger:
    """Initializes a rotating logger for wallet operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        # 5MB per file, keep 3 backup files
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

# Usage example
if __name__ == "__main__":
    log = setup_logger("wallet_utility_83")
    log.info("Logger initialized successfully")