import time
import urllib.request
import urllib.error
from functools import wraps
from typing import Callable, Any, Type, Tuple


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    exceptions: Tuple[Type[BaseException], ...] = (urllib.error.URLError, TimeoutError),
) -> Callable:
    """Decorator to retry network requests with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = 1.0
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        raise err
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator


@retry_network_op(max_retries=4, backoff_factor=2.0)
def fetch_blockchain_data(endpoint_url: str) -> str:
    """Fetch raw JSON payload from a remote blockchain API endpoint."""
    req = urllib.request.Request(
        endpoint_url,
        headers={"User-Agent": "wallet-utility-83/1.0"}
    )
    with urllib.request.urlopen(req, timeout=10) as response:
        return response.read().decode("utf-8")
