import logging
import functools
import time
from typing import Callable, Any

# Configure centralized logger for wallet-utility-83
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('wallet-utility-83')

_execution_cache = {}

def lru_cache_with_ttl(ttl_seconds: int = 300):
    """Decorator for performance optimization via timed memoization"""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, frozenset(kwargs.items()))
            now = time.time()
            
            if key in _execution_cache:
                result, timestamp = _execution_cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            _execution_cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def log_performance(func: Callable):
    """Wrapper to track execution latency for bottlenecks"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        if duration > 1.0:
            logger.warning(f"High latency detected in {func.__name__}: {duration:.4f}s")
        return result
    return wrapper