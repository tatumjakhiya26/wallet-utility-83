import re
from typing import Optional

class AddressValidationError(Exception):
    """Raised when a cryptocurrency address format is invalid."""
    pass

def validate_crypto_address(address: str, chain_type: str = 'btc') -> bool:
    """
    Validates cryptocurrency address formats using regex patterns.
    Raises AddressValidationError for malformed inputs.
    """
    if not isinstance(address, str) or not address:
        raise AddressValidationError("Address must be a non-empty string")

    patterns = {
        'btc': r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$',
        'eth': r'^0x[a-fA-F0-9]{40}$'
    }

    pattern = patterns.get(chain_type.lower())
    if not pattern:
        raise ValueError(f"Unsupported chain type: {chain_type}")

    try:
        if not re.match(pattern, address):
            raise AddressValidationError(f"Invalid {chain_type} address format")
    except re.error as e:
        raise AddressValidationError(f"Regex engine failure: {e}")

    return True

def sanitize_amount(amount: str) -> float:
    """
    Safely parses string amounts to float, handling malformed numeric input.
    """
    try:
        value = float(amount)
        if value < 0:
            raise ValueError("Negative amount provided")
        return value
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid numeric input: {e}")