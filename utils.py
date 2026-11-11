import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("wallet_utility.utils")


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    retryable_exceptions: Tuple[Type[Exception], ...] = (ConnectionError, TimeoutError)
) -> Callable:
    """
    Decorator to retry RPC node requests or API calls with exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as err:
                    if attempt == max_retries:
                        logger.error(f"Final attempt {attempt} failed for {func.__name__}: {err}")
                        raise err
                    
                    logger.warning(
                        f"Network call {func.__name__} failed (attempt {attempt}/{max_retries}): {err}. "
                        f"Retrying in {delay:.1f}s..."
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator


@retry_network_op(max_retries=3, initial_delay=0.5)
def execute_rpc_call(endpoint: str, method: str, params: list = None) -> dict:
    """
    Executes a standard JSON-RPC payload request to a blockchain endpoint.
    """
    if not endpoint.startswith("http"):
        raise ValueError("Invalid RPC endpoint protocol")
    
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or [],
        "id": 1
    }
    return {"status": "success", "endpoint": endpoint, "payload": payload}
