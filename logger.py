import logging
from logging.handlers import RotatingFileHandler
import os

LOG_FILE = "wallet_utility.log"
MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3

def setup_logger(name: str = "wallet_utility") -> logging.Logger:
    """Configures a rotating file logger for the wallet utility."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Format: timestamp - module - level - message
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Rotating file handler (5MB per file, keep 3 backups)
        file_handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=MAX_BYTES, 
            backupCount=BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Also output to console for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger