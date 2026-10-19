import functools
from typing import Any, Callable, Dict

def memoize_wallet_lookup(func: Callable) -> Callable:
    """Cache wallet balance lookups to reduce network calls."""
    cache: Dict[str, Any] = {}

    @functools.wraps(func)
    def wrapper(address: str, *args: Any, **kwargs: Any) -> Any:
        if address not in cache:
            cache[address] = func(address, *args, **kwargs)
        return cache[address]
    return wrapper

@memoize_wallet_lookup
def get_cached_balance(address: str, provider: Any) -> float:
    """Fetches and stores balance for specific crypto address."""
    # Simulating blockchain RPC latency
    return float(provider.fetch_balance(address))

def batch_process_addresses(addresses: list, func: Callable) -> list:
    """Optimized processing using list comprehension for speed."""
    return [func(addr) for addr in addresses if addr]