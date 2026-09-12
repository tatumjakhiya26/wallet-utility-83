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
                    if attempts == max_retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    time.sleep(delay * attempts)
        return wrapper
    return decorator

@retry_network_op(max_retries=3, delay=1)
def fetch_balance(address):
    # Simulated network call for crypto wallet balance
    logger.info(f"Fetching balance for {address}")
    return 0.0

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetch_balance("0xabc123")