import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
DEFAULT_LOG_FILE = LOG_DIR / "wallet_activity.log"
LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"


def setup_logger(
    name: str = "wallet_utility",
    log_file: Path | str = DEFAULT_LOG_FILE,
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,  # 5 MB per file
    backup_count: int = 5,
) -> logging.Logger:
    """Sets up a logger with console output and size-based file rotation."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers if logger is already configured
    if logger.handlers:
        return logger

    formatter = logging.Formatter(LOG_FORMAT)

    # Console Handler for real-time stdout streaming
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    # File Handler with rotation for persistent audit logs
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    file_handler = RotatingFileHandler(
        filename=log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    logger.debug(f"Logger '{name}' initialized with file: {log_path}")
    return logger


if __name__ == "__main__":
    # Demonstration of logger usage for transaction monitoring
    log = setup_logger()
    log.info("Crypto wallet service initialized")
    log.warning("High gas price detected on Ethereum network")
    log.info("Transaction 0x7a250d5630b4cf539739df2c5dacb4c659f2488d processed")
