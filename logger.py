import logging
import sys

# configure logging for wallet-utility-83 crypto operations
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

def get_wallet_logger(name: str) -> logging.Logger:
    """Factory to retrieve configured logger instance."""
    logger = logging.getLogger(name)
    return logger

def log_transaction_event(tx_hash: str, status: str, details: str = "") -> None:
    """Log standardized crypto transaction lifecycle events."""
    logger = get_wallet_logger("crypto_tx")
    msg = f"TXID: {tx_hash} | STATUS: {status}"
    if details:
        msg += f" | INFO: {details}"
    
    if status.upper() in ["FAILED", "ERROR"]:
        logger.error(msg)
    else:
        logger.info(msg)