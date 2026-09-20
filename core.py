import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(max_retries=3, delay=2):
    """Decorator for retrying unstable network operations."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    logger.warning(f"Attempt {attempts} failed: {e}. Retrying...")
                    if attempts == max_retries:
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry_network_op(max_retries=3, delay=1)
def fetch_balance(address):
    """Simulate fetching crypto balance with retry logic."""
    # Example implementation placeholder
    print(f"Fetching data for {address}")
    return 0.0