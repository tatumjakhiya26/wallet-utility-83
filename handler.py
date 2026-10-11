import time
import random
import logging
import json
import urllib.error
import urllib.request
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)


class NetworkError(Exception):
    """Custom exception for persistent network failures."""
    pass


def retry_network_op(
    max_retries: int = 3,
    base_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (urllib.error.URLError, TimeoutError, NetworkError)
) -> Callable:
    """Decorator to retry network requests with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = base_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(f"Failed '{func.__name__}' after {max_retries} attempts: {err}")
                        raise NetworkError(f"Operation {func.__name__} failed: {err}") from err
                    
                    jitter = random.uniform(0.05, 0.25)
                    sleep_time = (delay * backoff_factor) + jitter
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for '{func.__name__}' failed: {err}. "
                        f"Retrying in {sleep_time:.2f}s..."
                    )
                    time.sleep(sleep_time)
                    delay = sleep_time
        return wrapper
    return decorator


@retry_network_op(max_retries=3, base_delay=0.5)
def fetch_json_rpc(endpoint_url: str, payload: dict, timeout: int = 10) -> dict:
    """Executes a JSON-RPC request to a crypto node with automatic retries."""
    headers = {"Content-Type": "application/json"}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(endpoint_url, data=data, headers=headers, method="POST")

    with urllib.request.urlopen(req, timeout=timeout) as response:
        if response.status != 200:
            raise NetworkError(f"HTTP Status {response.status}")
        return json.loads(response.read().decode("utf-8"))
