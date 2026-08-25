import re
from functools import lru_cache
from typing import List, Dict

# Precompiled regex patterns for improved performance
ETH_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
BTC_PATTERN = re.compile(r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,39}$')

@lru_cache(maxsize=128)
def is_valid_eth_address(address: str) -> bool:
    """Validate Ethereum wallet address format.
    Caching avoids recomputation for same inputs.
    """
    if not isinstance(address, str):
        return False
    return ETH_PATTERN.match(address) is not None

@lru_cache(maxsize=128)
def is_valid_btc_address(address: str) -> bool:
    """Validate Bitcoin wallet address format.
    Uses cache for performance in high-volume checks.
    """
    if not isinstance(address, str):
        return False
    return BTC_PATTERN.match(address) is not None

def batch_validate(addresses: List[str], chain: str = "eth") -> Dict[str, bool]:
    """Batch validate multiple addresses efficiently.
    Leverages cached validators to speed up.
    """
    if chain == "eth":
        validator = is_valid_eth_address
    elif chain == "btc":
        validator = is_valid_btc_address
    else:
        raise ValueError(f"Unsupported chain: {chain}")
    return {addr: validator(addr) for addr in addresses}

def filter_valid_addresses(addresses: List[str], chain: str = "eth") -> List[str]:
    """Filter to only valid addresses.
    Optimized batch processing reduces overhead.
    """
    validated = batch_validate(addresses, chain)
    return [addr for addr, is_valid in validated.items() if is_valid]