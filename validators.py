import re

def validate_wallet_address(address: str) -> bool:
    """Validates standard crypto address format."""
    if not isinstance(address, str) or len(address) < 26 or len(address) > 42:
        return False
    return bool(re.match(r'^[a-zA-Z0-9]+$', address))

def validate_amount(amount: float) -> bool:
    """Checks if amount is a positive numeric value."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def process_input(data: dict) -> bool:
    """Main loop validation logic."""
    address = data.get("address")
    amount = data.get("amount")

    if not validate_wallet_address(str(address)):
        return False
    
    if not validate_amount(amount):
        return False

    return True