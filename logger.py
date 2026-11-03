import logging
import sys
from typing import Optional

# Configure centralized logger for wallet-utility-83
logger = logging.getLogger('wallet_utility')
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def log_error(context: str, error: Exception, critical: bool = False) -> None:
    """Handles logging of edge cases and exceptions during crypto ops."""
    error_type = type(error).__name__
    message = f"Error in {context}: [{error_type}] {str(error)}"
    
    if critical:
        logger.critical(message)
    else:
        logger.error(message)

def safe_log_operation(func):
    """Decorator for catching exceptions during wallet interactions."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, ConnectionError, TypeError) as e:
            log_error(func.__name__, e)
            return None
        except Exception as e:
            log_error(func.__name__, e, critical=True)
            raise
    return wrapper