import time
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def with_retry(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Executes network operations with exponential backoff."""
    last_exception = None
    
    for attempt in range(retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            wait_time = delay * (2 ** attempt)
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
        except Exception as e:
            logger.error(f"Non-retryable error encountered: {e}")
            raise
            
    logger.error(f"Operation failed after {retries} attempts")
    raise last_exception

def fetch_wallet_balance(api_client: Any, address: str) -> float:
    """Wrapper to retrieve balance with resiliency."""
    def operation():
        return api_client.get_balance(address)
    
    return with_retry(operation)