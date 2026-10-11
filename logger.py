import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

LOG_DIR = "logs"
DEFAULT_LOG_FILE = "wallet_utility.log"
DEFAULT_LOG_LEVEL = logging.INFO
MAX_BYTES = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 5


def setup_logger(
    name: str = "wallet_utility",
    log_file: Optional[str] = None,
    level: int = DEFAULT_LOG_LEVEL,
    max_bytes: int = MAX_BYTES,
    backup_count: int = BACKUP_COUNT,
) -> logging.Logger:
    """
    Configures and returns a Logger instance with console and rotating file handlers.
    Designed for tracking wallet operations and transaction logs securely.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers if logger is already configured
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    # Rotating File Handler
    if log_file is None:
        os.makedirs(LOG_DIR, exist_ok=True)
        log_file = os.path.join(LOG_DIR, DEFAULT_LOG_FILE)
    else:
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    return logger


# Pre-configured logger for general wallet operations
wallet_logger = setup_logger("wallet_core")
