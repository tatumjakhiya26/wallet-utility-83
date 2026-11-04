import re

def is_valid_address(address: str, chain: str = 'eth') -> bool:
    """Validate cryptocurrency address format based on network."""
    if not isinstance(address, str) or len(address) < 26:
        return False

    if chain == 'eth':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    if chain == 'btc':
        return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))
    
    return False

def is_valid_amount(amount: str) -> bool:
    """Validate numeric string representation for transaction."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def validate_tx_payload(data: dict) -> bool:
    """Check integrity of transaction request payload."""
    required = {'sender', 'recipient', 'amount', 'currency'}
    if not all(key in data for key in required):
        return False
        
    return is_valid_amount(data['amount']) and is_valid_address(data['recipient'])
