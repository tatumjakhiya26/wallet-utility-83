import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = "wallet.log") -> logging.Logger:
    """Configures a standard console and file logger for the wallet."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console output
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File output
    file_path = Path(log_file)
    file_handler = logging.FileHandler(file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Global instance for project-wide use
wallet_logger = setup_logger("wallet-utility-83")