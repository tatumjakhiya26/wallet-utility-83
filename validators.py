import re

def is_valid_ethereum_address(address: str) -> bool:
    """Validates standard Ethereum hexadecimal addresses."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def is_valid_amount(amount: str) -> bool:
    """Checks if string is a positive numeric decimal."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def sanitize_transaction_payload(payload: dict) -> dict:
    """Filters out invalid keys from transaction data."""
    allowed_keys = {'to', 'value', 'gas', 'data', 'nonce'}
    return {k: v for k, v in payload.items() if k in allowed_keys}

def validate_transaction_structure(tx: dict) -> bool:
    """Ensures mandatory fields exist in transaction."""
    required = {'to', 'value'}
    return all(key in tx for key in required)