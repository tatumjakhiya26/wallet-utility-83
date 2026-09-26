import logging
import sys
from typing import Optional

def setup_wallet_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures a standardized logger for wallet-utility-83 components.
    
    Args:
        name: The name of the logger instance.
        level: Logging level, defaults to INFO.
        
    Returns:
        Configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

def log_transaction_event(logger: logging.Logger, tx_hash: str, status: str) -> None:
    """
    Logs specific transaction lifecycle events for wallet operations.

    Args:
        logger: The logger instance to use.
        tx_hash: The cryptographic transaction hash.
        status: The current status of the transaction.
    """
    message: str = f"Transaction {tx_hash} updated to status: {status}"
    logger.info(message)