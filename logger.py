import logging
import sys
from typing import Optional

class WalletLogger:
    """Standardized logging utility for crypto operations."""

    def __init__(self, name: str = 'wallet-utility-83') -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, message: str, exc: Optional[Exception] = None) -> None:
        """Graceful handling of operational exceptions."""
        if exc:
            error_detail = f"{message}: {type(exc).__name__} - {str(exc)}"
            self.logger.error(error_detail)
        else:
            self.logger.error(message)

    def log_event(self, event: str, metadata: dict) -> None:
        """Sanitized logging of transaction metadata."""
        try:
            self.logger.info(f"EVENT: {event} | DATA: {str(metadata)}")
        except (ValueError, TypeError) as e:
            self.log_error("serialization failure during logging", e)

logger = WalletLogger()