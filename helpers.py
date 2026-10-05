import time
import random
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("wallet_utility.helpers")

def retry_on_failure(
    retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry a function on failure with exponential backoff and jitter.
    Useful for network calls to unstable crypto RPC nodes or APIs.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(f"Function {func.__name__} failed after {retries} attempts. Error: {e}")
                        raise e
                    
                    # Exponential backoff with jitter to prevent thundering herd problem
                    sleep_time = (backoff_factor * (2 ** (attempt - 1))) + random.uniform(0, 0.1)
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed for {func.__name__}: {e}. "
                        f"Retrying in {sleep_time:.2f} seconds..."
                    )
                    time.sleep(sleep_time)
        return wrapper
    return decorator
