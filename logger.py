import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = "wallet.log") -> logging.Logger:
    """Configures a standard logger for crypto wallet operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console handler for real-time visibility
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler for persistent transaction history
    log_path = Path(log_file)
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def log_transaction(logger: logging.Logger, tx_id: str, status: str, amount: float):
    """Utility to log specific wallet transaction events."""
    logger.info(f"Tx: {tx_id} | Status: {status} | Amount: {amount}")

# Global application logger
wallet_logger = setup_logger("wallet-utility-83")