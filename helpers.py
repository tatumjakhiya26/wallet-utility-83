import functools
import random
import time
from typing import Any, Callable, Tuple, Type


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    retry_exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """Decorator to retry network operations with exponential backoff and jitter.
    
    Useful for handling transient RPC node errors and rate limits in crypto applications.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retry_exceptions as err:
                    if attempt == max_retries:
                        raise err
                    
                    sleep_time = delay
                    if jitter:
                        sleep_time += random.uniform(0, 0.5 * delay)
                    
                    time.sleep(sleep_time)
                    delay *= backoff_factor
            return None
        return wrapper
    return decorator
