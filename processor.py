import time
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_on_failure(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry network operations with exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(f"Failed after {retries} attempts: {e}")
                        raise
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed: {e}. "
                        f"Retrying in {attempt_delay:.1f}s..."
                    )
                    time.sleep(attempt_delay)
                    attempt_delay *= backoff
        return wrapper
    return decorator

@retry_on_failure(retries=3, delay=1.0, backoff=2.0)
def fetch_api_data(url: str) -> str:
    """
    Fetches remote data with configured retry attempts.
    """
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "wallet-utility-83"})
    with urllib.request.urlopen(req, timeout=10) as response:
        return response.read().decode("utf-8")
