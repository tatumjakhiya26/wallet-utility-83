import re
from typing import Optional

def validate_address(address: str, chain_type: str = 'evm') -> bool:
    """
    Validates crypto wallet address formats for specified chains.
    
    Args:
        address: The wallet address string to check.
        chain_type: The blockchain network type (e.g., 'evm', 'btc').
        
    Returns:
        bool: True if address is valid, False otherwise.
    """
    if chain_type == 'evm':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    elif chain_type == 'btc':
        return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))
    return False

def validate_amount(amount: str) -> bool:
    """
    Checks if a string representation of an amount is a positive number.
    
    Args:
        amount: Numeric string to validate.
        
    Returns:
        bool: True if input is a valid decimal number greater than zero.
    """
    try:
        value = float(amount)
        return value > 0
    except ValueError:
        return False

def sanitize_memo(memo: str, max_length: int = 64) -> str:
    """
    Sanitizes transaction memos by stripping whitespace and enforcing limits.
    
    Args:
        memo: The raw memo string.
        max_length: Maximum allowed characters.
        
    Returns:
        str: The sanitized memo string.
    """
    clean_memo = re.sub(r'[^a-zA-Z0-9 ]', '', memo).strip()
    return clean_memo[:max_length]