import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts: int = 3, delay: float = 2.0):
    """Decorator to retry network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (2 ** attempt))
            logger.error(f"Operation failed after {max_attempts} attempts")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=1.0)
def fetch_balance(address: str):
    """Example of a network-bound wallet operation."""
    # Placeholder for actual network call logic
    return {"address": address, "balance": 0.0}