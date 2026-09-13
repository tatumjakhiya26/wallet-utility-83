import logging
import sys
from typing import Optional

def setup_crypto_logger(name: str = "wallet-utility-83") -> logging.Logger:
    """Configures logger with error handling for stream attachment."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        try:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        except (OSError, ValueError) as e:
            # Fallback to null handler if stdout is inaccessible
            logger.addHandler(logging.NullHandler())
            logger.critical(f"Logger initialization failure: {e}")

    return logger

def log_transaction_error(logger: logging.Logger, tx_id: Optional[str], error: Exception) -> None:
    """Structured logging for crypto transaction failures."""
    safe_id = tx_id or "UNKNOWN_TX"
    error_type = type(error).__name__
    
    logger.error(
        f"Transaction [{safe_id}] failed | Type: {error_type} | Details: {str(error)}"
    )

if __name__ == "__main__":
    # Example usage for testing
    test_logger = setup_crypto_logger()
    try:
        raise ConnectionError("Node RPC timeout")
    except Exception as e:
        log_transaction_error(test_logger, "0xabc123", e)