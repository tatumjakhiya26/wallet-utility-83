import re

# crypto-specific address patterns
ETH_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
BTC_PATTERN = re.compile(r'^(1|3|bc1)[a-zA-Z0-9]{25,39}$')

def validate_wallet_address(address: str, chain: str) -> bool:
    """verify address format based on network type."""
    if not isinstance(address, str):
        return False
    
    if chain.lower() == 'eth':
        return bool(ETH_PATTERN.match(address))
    if chain.lower() == 'btc':
        return bool(BTC_PATTERN.match(address))
    
    return False

def validate_amount(amount: float) -> bool:
    """ensure transaction amount is positive and numeric."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def process_transaction_input(data: dict) -> bool:
    """main entry point for input validation routines."""
    required_fields = ['address', 'amount', 'chain']
    if not all(field in data for field in required_fields):
        return False
        
    return (
        validate_wallet_address(data['address'], data['chain'])
        and validate_amount(data['amount'])
    )