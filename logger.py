import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "wallet_utility.log"
MAX_BYTES = 5 * 1024 * 1024  # 5MB
BACKUP_COUNT = 3

def setup_logger(name: str = "wallet-utility") -> logging.Logger:
    """Configures a rotating file logger for the application."""
    if not LOG_DIR.exists():
        LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup_logger is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Rotating file handler
        file_handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=MAX_BYTES, 
            backupCount=BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)
        
        # Console output for visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger