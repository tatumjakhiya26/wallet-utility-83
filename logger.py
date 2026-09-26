import logging
import re
import sys
from typing import Optional

# Pattern to detect private keys or sensitive seed phrases in log output
PRIVATE_KEY_PATTERN = re.compile(r"(?i)(private_?key|secret|seed_?phrase)[\s=:]+['"]?([a-zA-Z0-9]{32,64})['"]?")

class WalletAuditFormatter(logging.Formatter):
    """Custom formatter that redacts sensitive crypto data from log messages."""

    def format(self, record: logging.LogRecord) -> str:
        original_msg = super().format(record)
        # Redact private key patterns in logged output
        cleaned_msg = PRIVATE_KEY_PATTERN.sub(r"\1: [REDACTED]", original_msg)
        return cleaned_msg


def setup_logger(
    name: str = "wallet_utility",
    log_level: int = logging.INFO,
    log_file: Optional[str] = None
) -> logging.Logger:
    """Configures and returns a centralized logger instance for wallet operations."""
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    formatter = WalletAuditFormatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler if path is provided
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# Default logger instance for direct import
wallet_logger = setup_logger()
