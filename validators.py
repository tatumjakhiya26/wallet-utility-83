import re

def validate_address(address: str, chain: str = 'eth') -> bool:
    """Validates wallet address format based on network."""
    patterns = {
        'eth': r'^0x[a-fA-F0-9]{40}$',
        'btc': r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$'
    }
    pattern = patterns.get(chain)
    return bool(re.match(pattern, address)) if pattern else False

def validate_amount(amount: str) -> bool:
    """Ensures amount is a positive numeric string."""
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def process_transaction(data: dict) -> bool:
    """Main loop input validation handler."""
    required_fields = ['address', 'amount', 'chain']
    
    if not all(field in data for field in required_fields):
        return False
    
    if not validate_address(data['address'], data['chain']):
        return False
        
    if not validate_amount(data['amount']):
        return False
        
    return True