import os
import logging
from logging.handlers import RotatingFileHandler

DEFAULT_LOG_DIR = "logs"
DEFAULT_LOG_FILENAME = "wallet_utility.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB per log file
BACKUP_COUNT = 5                 # Keep up to 5 rolled log files


def setup_logger(
    name: str = "wallet_utility",
    log_dir: str = DEFAULT_LOG_DIR,
    log_filename: str = DEFAULT_LOG_FILENAME,
    level: int = logging.INFO,
    max_bytes: int = MAX_LOG_SIZE,
    backup_count: int = BACKUP_COUNT,
) -> logging.Logger:
    """Configures and returns a logger instance with file rotation and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if setup is called multiple times
    if logger.handlers:
        return logger

    # Ensure target output directory exists
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, log_filename)

    # Shared log entry formatter
    log_format = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Rotating File Handler for persistence
    file_handler = RotatingFileHandler(
        filename=log_file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(log_format)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    # Standard Console Handler for immediate CLI feedback
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    return logger


# Main logger instance for project module imports
wallet_logger = setup_logger()