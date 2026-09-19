import logging
import re
from typing import Optional


class CryptoMaskingFormatter(logging.Formatter):
    """Custom log formatter that scrubs private keys and secrets from output."""

    # Regex matching 64-character hex strings (common raw private key format)
    PRIVATE_KEY_REGEX = re.compile(r"\b(0x)?[a-fA-F0-9]{64}\b")

    def __init__(self, fmt: Optional[str] = None, datefmt: Optional[str] = None) -> None:
        super().__init__(fmt=fmt, datefmt=datefmt)

    def format(self, record: logging.LogRecord) -> str:
        """Formats log record while masking sensitive crypto key patterns.

        Args:
            record: The logging record instance.

        Returns:
            Formatted string with masked private keys.
        """
        original_msg = super().format(record)
        return self.PRIVATE_KEY_REGEX.sub("[MASKED_KEY]", original_msg)


def setup_logger(name: str = "wallet_utility", level: int = logging.INFO, log_file: Optional[str] = None) -> logging.Logger:
    """Configures a secure logger with masking for wallet operations.

    Args:
        name: Identifier for the logger instance.
        level: Logging verbosity level.
        log_file: Optional destination path for log output.

    Returns:
        Configured Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = CryptoMaskingFormatter(fmt=fmt)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger