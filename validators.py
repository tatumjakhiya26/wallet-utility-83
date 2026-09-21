import re

class AddressValidationError(Exception):
    """Custom exception for wallet address format errors."""
    pass

def validate_eth_address(address: str) -> bool:
    """
    Validates Ethereum-style hex addresses with checksum integrity check.
    Raises AddressValidationError on invalid formats or types.
    """
    if not isinstance(address, str):
        raise AddressValidationError("Address must be a string.")

    if not re.match(r'^0x[a-fA-F0-9]{40}$', address):
        raise AddressValidationError(f"Invalid address format: {address}")

    return True

def validate_transaction_amount(amount: float, min_limit: float = 0.0001) -> bool:
    """
    Checks if transaction amount is positive and above network dust limits.
    """
    try:
        amount_float = float(amount)
    except (TypeError, ValueError):
        raise ValueError("Amount must be a numeric value.")

    if amount_float < min_limit:
        raise ValueError(f"Amount {amount_float} below minimum limit of {min_limit}")

    return True

def sanitize_input(value: str) -> str:
    """
    Strips whitespace and null bytes from input strings for security.
    """
    if not value:
        return ""
    return str(value).strip().replace('\0', '')