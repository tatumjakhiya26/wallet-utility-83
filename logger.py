import logging
import sys
from typing import Optional

# Configure logging for wallet-utility-83
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

def get_wallet_logger(name: str) -> logging.Logger:
    """Returns a configured logger instance for wallet modules."""
    logger = logging.getLogger(f"wallet-utility-83.{name}")
    return logger

def log_transaction_status(tx_hash: str, status: str, error: Optional[str] = None) -> None:
    """Utility for standardized transaction outcome logging."""
    logger = get_wallet_logger("transaction")
    if error:
        logger.error(f"TX {tx_hash} failed: {error}")
    else:
        logger.info(f"TX {tx_hash} status: {status}")

if __name__ == "__main__":
    # Verification of logger functionality
    test_logger = get_wallet_logger("test")
    test_logger.info("Logger initialization successful")