import re

class AddressValidationError(Exception):
    """Custom exception for crypto address validation issues."""
    pass

def validate_eth_address(address: str) -> bool:
    """
    Validates Ethereum-like hex addresses with basic pattern matching.
    Ensures hex format and proper length constraints.
    """
    if not isinstance(address, str):
        raise AddressValidationError("Address must be a string")

    if not re.match(r"^0x[a-fA-F0-9]{40}$", address):
        raise AddressValidationError(f"Invalid Ethereum address format: {address}")

    return True

def validate_amount(amount: str) -> float:
    """
    Parses and validates numeric amount inputs for transaction safety.
    """
    try:
        value = float(amount)
        if value <= 0:
            raise ValueError("Amount must be a positive number")
        return value
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid transaction amount: {amount}") from e

def sanitize_input(data: str) -> str:
    """
    Strips whitespace and ensures data integrity before processing.
    """
    if not data:
        return ""
    return str(data).strip()