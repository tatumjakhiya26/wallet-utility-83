import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_retries=3, delay=2):
    """Decorator for retrying network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Operation failed after {max_retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=1)
def fetch_blockchain_data(endpoint):
    """Example network call wrapper for blockchain data."""
    # Placeholder for actual network request logic
    return {"status": "success", "endpoint": endpoint}