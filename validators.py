import re
from typing import Optional

def validate_address(address: str, chain_type: str = 'evm') -> bool:
    """Validates crypto wallet addresses based on chain constraints."""
    if not isinstance(address, str) or not address:
        return False

    if chain_type == 'evm':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    elif chain_type == 'btc':
        # Simple regex for Legacy/Segwit formats
        return bool(re.match(r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$', address))
    
    return False

def validate_amount(amount: str) -> Optional[float]:
    """Converts string amount to float with edge case checks."""
    try:
        val = float(amount)
        if val < 0:
            return None
        return val
    except (ValueError, TypeError):
        return None

def sanitize_input(data: str, max_length: int = 128) -> str:
    """Sanitizes input strings to prevent overflow or injection."""
    if not data:
        return ""
    cleaned = re.sub(r'[^a-zA-Z0-9_]', '', data)
    return cleaned[:max_length]