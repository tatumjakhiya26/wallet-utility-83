import logging
import os
import sys
from typing import Optional


class WalletFormatter(logging.Formatter):
    """Custom log formatter tailored for crypto wallet operations."""

    DEFAULT_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, fmt: Optional[str] = None):
        super().__init__(fmt=fmt or self.DEFAULT_FORMAT, datefmt=self.DATE_FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        # Ensure record message is formatted safely
        return super().format(record)


def get_logger(
    name: str = "wallet_utility",
    log_level: Optional[str] = None,
    log_file: Optional[str] = None,
) -> logging.Logger:
    """Configures and returns a standard application logger instance."""
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    level_name = log_level or os.getenv("WALLET_LOG_LEVEL", "INFO")
    numeric_level = getattr(logging, level_name.upper(), logging.INFO)
    logger.setLevel(numeric_level)

    formatter = WalletFormatter()

    # Console output handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Optional file logging handler
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# Default logger export for quick access
logger = get_logger()
