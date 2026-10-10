import functools
import re
from typing import Dict, Any

# Compiled regex for address validation to improve throughput
ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

@functools.lru_cache(maxsize=1024)
def is_valid_address(address: str) -> bool:
    """Validate hex address using cached pattern matching."""
    if not isinstance(address, str):
        return False
    return bool(ADDRESS_PATTERN.match(address))

def validate_transaction_batch(transactions: list) -> Dict[str, Any]:
    """Batch processing with memoization for repeated addresses."""
    results = {"valid": 0, "invalid": 0}
    for tx in transactions:
        addr = tx.get("to")
        if is_valid_address(addr):
            results["valid"] += 1
        else:
            results["invalid"] += 1
    return results

def clear_validation_cache():
    """Manual cache clearance for memory management."""
    is_valid_address.cache_clear()