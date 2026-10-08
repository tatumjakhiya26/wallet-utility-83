import re

def validate_address(address: str) -> bool:
    """Validate cryptocurrency wallet address format."""
    # Pattern for standard hex-based wallet addresses
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Verify input is a positive numerical value."""
    try:
        value = float(amount)
        return value > 0
    except ValueError:
        return False

def validate_transaction_data(address: str, amount: str) -> dict:
    """Check inputs for processing readiness."""
    errors = []
    if not validate_address(address):
        errors.append("Invalid wallet address format")
    if not validate_amount(amount):
        errors.append("Invalid amount: must be positive numeric")
    
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }