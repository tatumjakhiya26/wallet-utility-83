import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def with_retry(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            current_delay = delay
            
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed for {func.__name__}, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator