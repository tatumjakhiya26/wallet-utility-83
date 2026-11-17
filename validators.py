import re

# regex patterns for cryptocurrency wallet addresses
VALID_ADDRESS_PATTERNS = {
    'BTC': r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',
    'ETH': r'^0x[a-fA-F0-9]{40}$',
    'SOL': r'^[1-9A-HJ-NP-Za-km-z]{32,44}$'
}

def validate_wallet_address(address: str, chain: str) -> bool:
    """Checks if a wallet address matches the target chain format."""
    pattern = VALID_ADDRESS_PATTERNS.get(chain)
    if not pattern:
        raise ValueError(f"Unsupported chain type: {chain}")
    
    return bool(re.match(pattern, address))

def validate_transaction_amount(amount: float) -> bool:
    """Ensures transaction amount is positive and within limits."""
    return isinstance(amount, (int, float)) and 0 < amount < 1000000.0

def validate_input_data(data: dict) -> bool:
    """General input validation for processing loop."""
    required_keys = ['address', 'amount', 'chain']
    if not all(key in data for key in required_keys):
        return False
        
    if not validate_wallet_address(data['address'], data['chain']):
        return False
        
    if not validate_transaction_amount(data['amount']):
        return False
        
    return True