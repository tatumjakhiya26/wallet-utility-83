import re

class ValidationError(Exception):
    """Base class for validation errors in wallet-utility-83."""
    pass

def validate_address(address: str) -> bool:
    """Validates cryptocurrency address format (hex string)."""
    if not isinstance(address, str) or len(address) < 26 or len(address) > 42:
        raise ValidationError(f"Invalid address length: {address}")
    
    if not re.match(r"^0x[a-fA-F0-9]+$", address):
        raise ValidationError(f"Address must be hex string starting with 0x: {address}")
    
    return True

def validate_amount(amount: float) -> bool:
    """Ensures transaction amount is positive and non-zero."""
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValidationError(f"Amount must be a positive number: {amount}")
    
    return True

def process_input(address: str, amount: float):
    """Validates inputs before entering the main processing loop."""
    try:
        validate_address(address)
        validate_amount(amount)
    except ValidationError as e:
        # Log or re-raise based on integration requirements
        print(f"Validation failed: {e}")
        raise