import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts: int = 3, delay: float = 2.0):
    """Decorator for retrying unstable network calls."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            logger.error(f"Operation failed after {max_attempts} attempts.")
            raise last_exception
        return wrapper
    return decorator