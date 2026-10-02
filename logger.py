import logging
import re
import sys


class SensitiveDataFilter(logging.Filter):
    """Filter that masks sensitive crypto keys and long hex strings in log records."""

    # Matches potential private keys or long secret strings (64 hex chars)
    SECRET_PATTERN = re.compile(r"\b(0x)?[a-fA-F0-9]{64}\b")

    def filter(self, record: logging.LogRecord) -> bool:
        if isinstance(record.msg, str):
            record.msg = self.SECRET_PATTERN.sub("[REDACTED_SECRET]", record.msg)
        if record.args:
            if isinstance(record.args, dict):
                record.args = {
                    k: (
                        self.SECRET_PATTERN.sub("[REDACTED_SECRET]", str(v))
                        if isinstance(v, str)
                        else v
                    )
                    for k, v in record.args.items()
                }
            elif isinstance(record.args, tuple):
                record.args = tuple(
                    self.SECRET_PATTERN.sub("[REDACTED_SECRET]", str(arg))
                    if isinstance(arg, str)
                    else arg
                    for arg in record.args
                )
        return True


def setup_logger(
    name: str = "wallet_utility", level: int = logging.INFO
) -> logging.Logger:
    """Configures and returns a logger instance with sensitive data masking."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers if already initialized
    if logger.handlers:
        return logger

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler.setFormatter(formatter)
    handler.addFilter(SensitiveDataFilter())

    logger.addHandler(handler)
    logger.propagate = False

    return logger


# Default logger instance for quick access
wallet_logger = setup_logger()
