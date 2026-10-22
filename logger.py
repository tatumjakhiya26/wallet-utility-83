import logging
import re
import sys
from typing import Optional

# Sensitive patterns to mask in crypto logs (private keys, mnemonics)
SENSITIVE_PATTERNS = [
    (r"(0x)?[a-fA-F0-9]{64}", "[MASKED_PRIVATE_KEY]"),
    (r"\b(?:[a-z]+\s+){11}[a-z]+\b", "[MASKED_MNEMONIC]"),
]


class CryptoSanitizingFormatter(logging.Formatter):
    """Log formatter that masks sensitive crypto data like private keys and seed phrases."""

    def __init__(self, fmt: Optional[str] = None, datefmt: Optional[str] = None):
        super().__init__(fmt, datefmt)

    def format(self, record: logging.LogRecord) -> str:
        original_msg = super().format(record)
        sanitized_msg = original_msg

        for pattern, replacement in SENSITIVE_PATTERNS:
            sanitized_msg = re.sub(pattern, replacement, sanitized_msg)

        return sanitized_msg


def setup_logger(
    name: str = "wallet_utility", level: int = logging.INFO
) -> logging.Logger:
    """Configures and returns a sanitized logger for wallet operations."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        fmt = "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
        formatter = CryptoSanitizingFormatter(fmt=fmt, datefmt="%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


# Default logger instance for direct module imports
default_logger = setup_logger()
