import logging
import sys
from typing import Optional

class WalletLogger:
    """Centralized logger for wallet-utility-83"""
    def __init__(self, name: str = "wallet_util"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, message: str, exc: Optional[Exception] = None) -> None:
        """Handles logging with optional exception context"""
        if exc:
            self.logger.error(f"{message} | Error: {type(exc).__name__} | {str(exc)}")
        else:
            self.logger.error(message)

    def safe_execute(self, func, *args, **kwargs):
        """Wrapper to catch execution errors"""
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, ConnectionError) as e:
            self.log_error(f"Execution failure in {func.__name__}", e)
            return None
        except Exception as e:
            self.log_error("Critical unexpected failure", e)
            raise