import os
import logging
from logging.handlers import RotatingFileHandler

DEFAULT_LOG_DIR = "logs"
DEFAULT_LOG_FILE = "wallet.log"
MAX_BYTES = 5 * 1024 * 1024  # 5 MB per log file
BACKUP_COUNT = 5


def setup_logger(
    name: str = "wallet_utility",
    log_dir: str = DEFAULT_LOG_DIR,
    log_file: str = DEFAULT_LOG_FILE,
    level: int = logging.INFO,
    max_bytes: int = MAX_BYTES,
    backup_count: int = BACKUP_COUNT,
) -> logging.Logger:
    """Configures and returns a logger instance with console and rotating file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding duplicate handlers if function is called multiple times
    if logger.handlers:
        return logger

    os.makedirs(log_dir, exist_ok=True)
    file_path = os.path.join(log_dir, log_file)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


wallet_logger = setup_logger()
