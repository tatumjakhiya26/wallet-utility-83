import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_call(max_retries: int = 3, delay: float = 1.0) -> Callable:
    """Decorator for retrying unstable network operations with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            current_delay = delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    retries += 1
                    if retries == max_retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Retry {retries}/{max_retries} for {func.__name__} after {current_delay}s")
                    time.sleep(current_delay)
                    current_delay *= 2
        return wrapper
    return decorator