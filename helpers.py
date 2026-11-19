import time
import logging
from typing import Optional, Dict

logger = logging.getLogger(__name__)

def format_address(address: str) -> str:
    """Truncate crypto address for display."""
    if len(address) > 12:
        return f"{address[:6]}...{address[-4:]}"
    return address

def validate_gas_price(price_gwei: float) -> bool:
    """Ensure gas prices are within sane network limits."""
    return 0.1 <= price_gwei <= 1000.0

def retry_on_failure(retries: int = 3, delay: float = 1.0):
    """Decorator for transient network request retries."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_ex = None
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    time.sleep(delay * (i + 1))
            logger.error(f"Failed after {retries} attempts: {last_ex}")
            raise last_ex
        return wrapper
    return decorator

def sanitize_tx_data(data: Dict) -> Dict:
    """Remove empty or null fields from transaction payload."""
    return {k: v for k, v in data.items() if v is not None}