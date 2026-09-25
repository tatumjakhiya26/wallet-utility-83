import time
import logging
import functools
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_op(retries: int = 3, delay: float = 2.0, backoff: float = 1.5):
    """Decorator for retrying unstable network operations."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s: {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=1.0)
def fetch_wallet_balance(address: str):
    """Example usage for network-dependent wallet fetch."""
    # Simulating actual network call
    logger.info(f"Fetching balance for {address}")
    # raise ConnectionError("Service unavailable") 
    return 0.0