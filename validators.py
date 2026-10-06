import re
from typing import Optional

class AddressValidationError(Exception):
    """Custom exception for crypto address validation failures."""
    pass

def validate_eth_address(address: str) -> bool:
    """Validates Ethereum address format with edge case handling."""
    if not isinstance(address, str):
        raise AddressValidationError("Address must be a string")
    
    if not address:
        raise AddressValidationError("Address string is empty")
        
    # Check hex format and length (42 chars starting with 0x)
    pattern = r'^0x[a-fA-F0-9]{40}$'
    if not re.match(pattern, address):
        raise AddressValidationError(f"Invalid address format: {address}")
        
    return True

def sanitize_amount(amount: str) -> float:
    """Converts string amount to float with input sanitization."""
    try:
        clean_amount = amount.strip().replace(',', '')
        value = float(clean_amount)
        if value < 0:
            raise ValueError("Negative amount provided")
        return value
    except (ValueError, TypeError, AttributeError) as e:
        raise AddressValidationError(f"Invalid balance format: {e}")