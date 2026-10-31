import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(max_retries=3, delay=2, backoff=2):
    """
    Decorator to retry network operations with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            current_delay = delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    retries += 1
                    if retries >= max_retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Retry {retries}/{max_retries} for {func.__name__} after {current_delay}s")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator