import functools
from typing import Callable, Any, Dict
import time

# Cache for address validation results to improve lookup performance
_address_cache: Dict[str, bool] = {}

@functools.lru_cache(maxsize=1024)
def validate_address_format(address: str) -> bool:
    """Validate cryptocurrency address structure using cached pattern checks."""
    if not isinstance(address, str) or len(address) < 26 or len(address) > 42:
        return False
    return address.startswith('0x') or address.startswith('bc1')

def batch_process_wallets(addresses: list, func: Callable) -> list:
    """Execute processing on a list using list comprehensions for speed."""
    return [func(addr) for addr in addresses if validate_address_format(addr)]

class PerformanceTimer:
    """Context manager for tracking core module latency."""
    def __init__(self, operation_name: str):
        self.name = operation_name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        # Log performance metrics in a production scenario
        print(f"Operation {self.name} took {self.end - self.start:.6f}s")