import functools
from typing import Dict, Any, List

# Cache for address parsing results to reduce redundant compute
@functools.lru_cache(maxsize=1024)
def validate_and_normalize(address: str) -> str:
    """Normalizes and validates crypto addresses."""
    if not address or len(address) < 26:
        raise ValueError("invalid address length")
    return address.strip().lower()

class TransactionProcessor:
    def __init__(self):
        self._batch_size = 500

    def process_batch(self, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Optimized batch processing using list comprehension."""
        processed = []
        for tx in transactions:
            try:
                # Utilizing cached validation for frequent addresses
                raw_addr = tx.get("address", "")
                normalized = validate_and_normalize(raw_addr)
                
                processed.append({
                    "id": tx.get("id"),
                    "addr": normalized,
                    "amount": float(tx.get("amount", 0)),
                    "processed": True
                })
            except (ValueError, TypeError):
                continue
        return processed

    def clear_cache(self):
        """Manual cache invalidation for memory management."""
        validate_and_normalize.cache_clear()