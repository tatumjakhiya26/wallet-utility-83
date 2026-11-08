import re

# Validation patterns for crypto wallet operations
ADDRESS_PATTERN = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$|^0x[a-fA-F0-9]{40}$')
AMOUNT_MIN = 0.00000001

def validate_wallet_address(address: str) -> bool:
    """Verify address format for supported chains."""
    return bool(ADDRESS_PATTERN.match(address))

def validate_transaction_amount(amount: float) -> bool:
    """Ensure amount meets dust limits and is positive."""
    try:
        return float(amount) >= AMOUNT_MIN
    except (ValueError, TypeError):
        return False

def validate_input_data(data: dict) -> tuple[bool, str]:
    """Run checks against incoming transaction dictionary."""
    if 'address' not in data or not validate_wallet_address(data['address']):
        return False, "invalid wallet address"
    
    if 'amount' not in data or not validate_transaction_amount(data['amount']):
        return False, "invalid or insufficient transaction amount"
        
    return True, "success"