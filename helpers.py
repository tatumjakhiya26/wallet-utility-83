import re

def validate_address(address: str, chain: str) -> bool:
    """Validates crypto address format based on blockchain type."""
    patterns = {
        "eth": r"^0x[a-fA-F0-9]{40}$",
        "btc": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    }
    pattern = patterns.get(chain.lower())
    if not pattern:
        return False
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Checks if provided amount is a positive numeric string."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def process_input(raw_addr: str, raw_amt: str, chain: str) -> dict:
    """Validates transaction inputs before processing."""
    if not validate_address(raw_addr, chain):
        return {"status": "error", "message": "invalid address format"}
    
    if not validate_amount(raw_amt):
        return {"status": "error", "message": "invalid amount provided"}
        
    return {
        "status": "success", 
        "data": {"address": raw_addr, "amount": float(raw_amt)}
    }