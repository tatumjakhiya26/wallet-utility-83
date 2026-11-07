import re

def is_valid_address(address: str, chain: str = 'eth') -> bool:
    """Validate cryptocurrency address format based on network."""
    if not isinstance(address, str):
        return False

    if chain == 'eth':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    elif chain == 'btc':
        return bool(re.match(r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$', address))
    
    return False

def is_valid_amount(amount: str) -> bool:
    """Ensure amount is a positive numeric string."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def validate_transaction_data(data: dict) -> bool:
    """Verify required fields for blockchain transactions."""
    required_fields = {'sender', 'recipient', 'amount', 'currency'}
    if not all(field in data for field in required_fields):
        return False
    
    return is_valid_address(data['sender']) and is_valid_address(data['recipient'])
