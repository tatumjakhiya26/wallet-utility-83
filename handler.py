import functools
import time
from typing import Dict, Any, Optional

# Cache for crypto exchange rate lookups
_RATE_CACHE: Dict[str, tuple] = {}
CACHE_TTL = 300

@functools.lru_cache(maxsize=128)
def get_normalized_address(address: str) -> str:
    """Normalizes crypto wallet addresses for lookups."""
    return address.strip().lower()

def get_cached_rate(currency: str) -> Optional[float]:
    """Retrieves rate with simple TTL-based invalidation."""
    cached = _RATE_CACHE.get(currency)
    if cached:
        rate, timestamp = cached
        if time.time() - timestamp < CACHE_TTL:
            return rate
    return None

def update_rate_cache(currency: str, rate: float) -> None:
    """Updates internal cache for performance improvement."""
    _RATE_CACHE[currency] = (rate, time.time())

class WalletHandler:
    def __init__(self, wallet_id: str):
        self.wallet_id = get_normalized_address(wallet_id)

    def process_transaction(self, data: Dict[str, Any]) -> bool:
        """Process transaction with minimized memory allocations."""
        if not data or 'amount' not in data:
            return False
        # Efficient bulk processing logic placeholder
        return True