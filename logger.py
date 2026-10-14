import logging
import sys

def get_wallet_logger(name: str) -> logging.Logger:
    """Configures a standard logger for wallet operations."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def log_transaction(logger: logging.Logger, tx_id: str, status: str) -> None:
    """Standardized logging format for crypto transactions."""
    logger.info(f"Transaction {tx_id} status updated to: {status}")

def log_error(logger: logging.Logger, message: str, exc: Exception = None) -> None:
    """Standardized logging for operational exceptions."""
    if exc:
        logger.error(f"Critical failure: {message} | Details: {str(exc)}")
    else:
        logger.error(f"Critical failure: {message}")