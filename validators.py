import re

class ValidationError(Exception):
    """Base class for validation errors in wallet-utility-83."""
    pass

def validate_address(address: str, chain_type: str = 'eth') -> bool:
    """Validates cryptocurrency addresses for supported networks."""
    if not isinstance(address, str):
        raise ValidationError("Address must be a string.")

    patterns = {
        'eth': r'^0x[a-fA-F0-9]{40}$',
        'btc': r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$'
    }

    pattern = patterns.get(chain_type.lower())
    if not pattern:
        raise ValidationError(f"Unsupported chain type: {chain_type}")

    if not re.match(pattern, address):
        raise ValidationError(f"Invalid {chain_type} address format: {address}")

    return True

def validate_amount(amount: float) -> bool:
    """Checks if the transaction amount is positive and finite."""
    try:
        if amount <= 0:
            raise ValidationError("Transaction amount must be positive.")
        if not float(amount): 
            raise ValidationError("Amount must be a valid numeric value.")
    except (TypeError, ValueError):
        raise ValidationError("Invalid numeric input for transaction amount.")

    return True