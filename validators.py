import re
from typing import Any


def is_valid_eth_address(address: str) -> bool:
    """Validate Ethereum address format (40 hex characters with 0x prefix)."""
    if not isinstance(address, str):
        return False
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(pattern, address))


def is_valid_btc_address(address: str) -> bool:
    """Validate basic Bitcoin legacy, SegWit, and Native SegWit address formats."""
    if not isinstance(address, str):
        return False
    pattern = r"^(1|3|bc1q)[a-zA-HJ-NP-Z0-9]{25,62}$"
    return bool(re.match(pattern, address))


def is_valid_private_key(key: str) -> bool:
    """Check if a string is a 64-character raw hex private key."""
    if not isinstance(key, str):
        return False
    clean_key = key.lower().removeprefix("0x")
    return len(clean_key) == 64 and all(c in "0123456789abcdef" for c in clean_key)


def is_valid_tx_hash(tx_hash: str) -> bool:
    """Validate standard 32-byte (64 hex character) transaction hash."""
    if not isinstance(tx_hash, str):
        return False
    clean_hash = tx_hash.lower().removeprefix("0x")
    return len(clean_hash) == 64 and all(c in "0123456789abcdef" for c in clean_hash)


def validate_amount(amount: Any, min_amount: float = 0.0) -> bool:
    """Ensure numerical amount is valid and strictly greater than threshold."""
    try:
        val = float(amount)
        return val > min_amount
    except (ValueError, TypeError):
        return False
