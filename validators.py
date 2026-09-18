import re
from typing import Optional

# crypto address validation patterns
ADDRESS_PATTERNS = {
    'btc': r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$',
    'eth': r'^0x[a-fA-F0-9]{40}$',
    'sol': r'^[1-9A-HJ-NP-Za-km-z]{32,44}$'
}

def validate_address(address: str, chain_type: str) -> bool:
    """verify crypto address against chain-specific regex"""
    pattern = ADDRESS_PATTERNS.get(chain_type.lower())
    if not pattern:
        return False
    return bool(re.match(pattern, address))

def sanitize_amount(amount: str) -> Optional[float]:
    """clean string input and convert to float"""
    try:
        cleaned = re.sub(r'[^0-9.]', '', amount)
        return float(cleaned)
    except (ValueError, TypeError):
        return None

def validate_tx_hash(tx_hash: str) -> bool:
    """validate generic 64-character hex transaction hash"""
    return bool(re.match(r'^0x[a-fA-F0-9]{64}$', tx_hash))