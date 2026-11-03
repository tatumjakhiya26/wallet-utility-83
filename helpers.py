import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    retryable_exceptions: Tuple[Type[Exception], ...] = (ConnectionError, TimeoutError, OSError)
) -> Callable:
    """
    Decorator to retry network operations with exponential backoff and optional jitter.
    Designed for crypto RPC endpoints and API requests.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as exc:
                    if attempt == max_retries:
                        logger.error(
                            f"[RPC/API] '{func.__name__}' failed after {max_retries} attempts: {exc}"
                        )
                        raise
                    
                    # Calculate wait time with optional 20% jitter
                    sleep_time = delay * (random.uniform(0.8, 1.2) if jitter else 1.0)
                    logger.warning(
                        f"[RPC/API] Network call '{func.__name__}' failed (attempt {attempt}/{max_retries}): {exc}. "
                        f"Retrying in {sleep_time:.2f} seconds..."
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor
            
        return wrapper
    return decorator
