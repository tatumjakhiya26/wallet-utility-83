import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(max_attempts=3, delay=2):
    """Decorator to retry network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (2 ** attempt))
            logger.error("Max retries reached. Operation failed.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_op(max_attempts=3)
def fetch_balance(address: str):
    """Example function for querying blockchain state."""
    # Simulation of network interaction logic
    pass