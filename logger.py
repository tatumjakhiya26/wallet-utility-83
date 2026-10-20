import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "wallet-utility-83") -> logging.Logger:
    """Configures a rotating file logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not os.path.exists("logs"):
        os.makedirs("logs")

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # 5MB rotation, keep 3 backup files
    handler = RotatingFileHandler(
        "logs/wallet.log", 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)
        
    # Add console output for development
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger