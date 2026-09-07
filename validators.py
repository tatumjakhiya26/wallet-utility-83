import re
from typing import Optional

class AddressValidationError(Exception):
    """Raised when a crypto address format is invalid."""
    pass

def validate_wallet_address(address: str, chain_type: str = 'evm') -> bool:
    """
    Validates wallet address strings with specific regex patterns.
    Raises AddressValidationError on empty inputs or pattern mismatch.
    """
    if not address or not isinstance(address, str):
        raise AddressValidationError("Address must be a non-empty string")

    patterns = {
        'evm': r'^0x[a-fA-F0-9]{40}$',
        'btc': r'^(1|3|bc1)[a-zA-Z0-9]{25,39}$'
    }

    pattern = patterns.get(chain_type.lower())
    if not pattern:
        raise ValueError(f"Unsupported chain type: {chain_type}")

    if not re.match(pattern, address):
        raise AddressValidationError(f"Invalid {chain_type} address format")

    return True

def sanitize_amount(amount: str) -> float:
    """
    Converts string amount to float with boundary error handling.
    """
    try:
        value = float(amount)
        if value < 0:
            raise ValueError("Negative amount provided")
        return value
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid numerical amount: {e}")