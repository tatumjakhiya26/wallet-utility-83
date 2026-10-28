import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = "wallet.log", level: int = logging.INFO) -> logging.Logger:
    """Configures a standard logger for wallet-utility-83 operations."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

def get_app_logger() -> logging.Logger:
    """Factory for application-wide logging instances."""
    return setup_logger("wallet-utility")