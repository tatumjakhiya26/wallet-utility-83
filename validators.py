import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("wallet_utility.validators")

def retry_on_failure(
    retries: int = 3,
    backoff_in_seconds: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry a function call if specified exceptions are raised.
    Uses exponential backoff for network operations resilience.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            delay = backoff_in_seconds
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(f"Function {func.__name__} failed after {retries} attempts.")
                        raise e
                    logger.warning(
                        f"Retrying {func.__name__} due to {e.__class__.__name__}: {e}. "
                        f"Attempt {attempt}/{retries}. Retrying in {delay}s..."
                    )
                    time.sleep(delay)
                    delay *= 2
            return func(*args, **kwargs)
        return wrapper
    return decorator
