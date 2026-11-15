import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_op(retries: int = 3, backoff: float = 2.0):
    """
    Decorator for retrying network operations with exponential backoff.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            delay = 1.0
            
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay)
                    delay *= backoff
            
            logger.error("Max retries exceeded for network operation.")
            raise last_exception
        return wrapper
    return decorator