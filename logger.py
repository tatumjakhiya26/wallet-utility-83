import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(
    name: str = "wallet_utility",
    log_file: str = "logs/wallet.log",
    level: int = logging.INFO
) -> logging.Logger:
    """
    Configures and returns a logger with console and rotating file outputs.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding handlers multiple times if logger already configured
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s"
        )

        # Create directory for log file if it does not exist
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        # Rotating file handler (rotates at 5MB, keeps last 5 logs)
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

        # Stream handler for console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)
        logger.addHandler(console_handler)

    return logger