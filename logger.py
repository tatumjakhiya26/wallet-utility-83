import os
import logging
from logging.handlers import RotatingFileHandler

# Default log directory and settings for wallet operations
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "wallet_utility.log")
MAX_LOG_BYTES = 5 * 1024 * 1024  # 5 MB per file
BACKUP_COUNT = 5  # Retain up to 5 archived logs

def setup_logger(name: str = "wallet_utility", level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a logger instance with file rotation and console output."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding duplicate handlers if logger is initialized multiple times
    if logger.handlers:
        return logger

    # Standard log format for tracking transaction events and utility status
    formatter = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    # Rotating File Handler
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=MAX_LOG_BYTES,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    return logger

# Default module-level logger for instant import
logger = setup_logger()
