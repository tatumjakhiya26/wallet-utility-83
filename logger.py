import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = 'wallet.log', level: int = logging.INFO) -> logging.Logger:
    """
    Configures a standard logger for crypto wallet operations.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler for real-time monitoring
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler for audit logs
    file_path = Path(log_file)
    file_handler = logging.FileHandler(file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def get_wallet_logger() -> logging.Logger:
    """
    Returns a pre-configured logger instance for the application.
    """
    return setup_logger('wallet-utility-83')