import re
from typing import Optional

# regex for common evm address format
ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_address(address: str) -> bool:
    """verify crypto wallet address format"""
    if not address or not isinstance(address, str):
        return False
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: str) -> bool:
    """verify numeric precision for transactions"""
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def sanitize_input(user_input: str) -> str:
    """strip whitespace and normalize encoding"""
    return str(user_input).strip()

def process_transaction_input(address: str, amount: str) -> Optional[dict]:
    """data validation gate for transaction processing"""
    clean_address = sanitize_input(address)
    clean_amount = sanitize_input(amount)

    if not validate_address(clean_address):
        return None
    
    if not validate_amount(clean_amount):
        return None

    return {
        "address": clean_address,
        "amount": float(clean_amount)
    }