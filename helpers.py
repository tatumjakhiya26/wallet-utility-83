import re

def validate_address(address: str, chain: str) -> bool:
    """Validate crypto address format based on network type."""
    patterns = {
        "eth": r"^0x[a-fA-F0-9]{40}$",
        "btc": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    }
    pattern = patterns.get(chain.lower())
    if not pattern:
        return False
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Ensure input is a positive numerical string."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def process_transaction_input(address: str, chain: str, amount: str) -> dict:
    """Validate and structure user inputs for processing."""
    if not validate_address(address, chain):
        raise ValueError(f"Invalid {chain} address format")
    
    if not validate_amount(amount):
        raise ValueError("Amount must be a positive number")
        
    return {
        "address": address.strip(),
        "chain": chain.lower().strip(),
        "amount": float(amount)
    }