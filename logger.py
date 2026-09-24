import logging
import sys
from typing import Optional

def setup_crypto_logger(name: str = "wallet-utility-83") -> logging.Logger:
    """
    Configures a standardized logger for crypto operations.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_transaction_status(logger: logging.Logger, tx_id: str, status: str, details: Optional[str] = None) -> None:
    """
    Logs structured transaction lifecycle updates.
    """
    message = f"TX[{tx_id}] - status: {status}"
    if details:
        message += f" | details: {details}"
    
    if status.lower() in ["failed", "error", "rejected"]:
        logger.error(message)
    else:
        logger.info(message)

# Instantiate default utility logger
crypto_logger = setup_crypto_logger()