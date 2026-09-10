import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_op(max_retries: int = 3, backoff_factor: float = 1.5, exceptions: tuple = (ConnectionError, TimeoutError)):
    """
    Decorator to retry network operations with exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = 1.0
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(f"Operation {func.__name__} failed after {max_retries} attempts: {err}")
                        raise
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} failed for {func.__name__}: {err}. Retrying in {delay:.1f}s..."
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator

class NetworkHandler:
    """Handles RPC and node network requests for wallet actions."""
    
    def __init__(self, endpoint_url: str):
        self.endpoint_url = endpoint_url

    @retry_network_op(max_retries=3, backoff_factor=2.0)
    def query_balance(self, address: str) -> dict:
        """Query wallet balance over RPC endpoint with automatic retries."""
        if not address.startswith("0x") or len(address) != 42:
            raise ValueError("Invalid Ethereum address string")
            
        # Simulated payload for wallet utility
        return {"address": address, "status": "active", "balance_wei": 1000000000000000000}
