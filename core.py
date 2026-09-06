import functools
import time
from typing import Dict, Any

# Cache dictionary to avoid redundant balance calculations
_balance_cache: Dict[str, Any] = {}
CACHE_TTL = 30

def get_memoized_balance(wallet_id: str, fetch_func: callable) -> float:
    """Fetches balance with simple TTL-based cache optimization."""
    current_time = time.time()
    
    if wallet_id in _balance_cache:
        data, timestamp = _balance_cache[wallet_id]
        if current_time - timestamp < CACHE_TTL:
            return data
            
    # Update cache with fresh data
    balance = fetch_func(wallet_id)
    _balance_cache[wallet_id] = (balance, current_time)
    return balance

def clear_cache() -> None:
    """Clears local memory cache."""
    _balance_cache.clear()

@functools.lru_cache(maxsize=128)
def get_wallet_metadata(wallet_id: str) -> Dict[str, str]:
    """Expensive metadata lookup optimized via LRU cache."""
    # Simulating network latency or DB overhead
    return {"id": wallet_id, "network": "mainnet", "status": "active"}