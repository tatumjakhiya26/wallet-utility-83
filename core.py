import time
import functools
import logging

# Set up logger for network operations
logger = logging.getLogger('wallet-utility-83')

def retry_network_op(retries=3, delay=2, backoff=2):
    """
    Decorator for retrying unstable crypto network requests.
    :param retries: Number of attempts
    :param delay: Initial delay in seconds
    :param backoff: Multiplier for delay after each failure
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries:
                        logger.error(f'Final attempt failed for {func.__name__}')
                        raise
                    
                    logger.warning(f'Attempt {attempt} failed, retrying in {current_delay}s...')
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_op(retries=3)
def fetch_balance(address: str):
    # Simulate network call logic here
    logger.info(f'Fetching balance for {address}')
    return {'address': address, 'balance': 0.0}