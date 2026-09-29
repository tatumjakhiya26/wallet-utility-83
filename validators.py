import re

def validate_address(address: str, network: str = 'mainnet') -> bool:
    """Validate crypto wallet address format."""
    patterns = {
        'bitcoin': r'^(1|3|bc1)[a-zA-Z0-9]{25,59}$',
        'ethereum': r'^0x[a-fA-F0-9]{40}$'
    }
    pattern = patterns.get(network.lower())
    if not pattern:
        return False
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Validate numeric format for transaction amounts."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def validate_payload(data: dict) -> bool:
    """Check mandatory fields in processing payload."""
    required = ['address', 'amount', 'currency']
    return all(key in data for key in required)

def sanitize_input(user_input: str) -> str:
    """Remove whitespace and force lowercase for processing."""
    return user_input.strip().lower()