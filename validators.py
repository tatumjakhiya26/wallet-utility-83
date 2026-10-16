import time
import functools
import requests
from typing import Callable, Any

def retry_network_operation(max_attempts: int = 3, delay: float = 1.0):
    """Decorator to retry network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (2 ** attempt))
                        continue
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=2.0)
def fetch_wallet_balance(api_url: str) -> dict:
    """Fetches balance with built-in retry logic."""
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()
    return response.json()