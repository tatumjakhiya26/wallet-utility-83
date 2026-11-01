import re

def validate_address(address: str) -> bool:
    """Validate cryptocurrency wallet address format."""
    # Pattern for standard hex wallet addresses
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Validate positive decimal amount input."""
    try:
        value = float(amount)
        return value > 0
    except ValueError:
        return False

def sanitize_input(user_input: str) -> str:
    """Remove whitespace and escape potential script injections."""
    return user_input.strip().replace('<', '').replace('>', '')

def process_transaction(address: str, amount: str):
    """Main processing loop entry with input validation."""
    clean_addr = sanitize_input(address)
    clean_amt = sanitize_input(amount)

    if not validate_address(clean_addr):
        raise ValueError(f"Invalid wallet address format: {clean_addr}")
    
    if not validate_amount(clean_amt):
        raise ValueError(f"Invalid transaction amount: {clean_amt}")

    return {
        "address": clean_addr,
        "amount": float(clean_amt),
        "status": "validated"
    }