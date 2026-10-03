import re

# Crypto address validation patterns
ADDRESS_PATTERNS = {
    'bitcoin': r'^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$',
    'ethereum': r'^0x[a-fA-F0-9]{40}$'
}

def is_valid_address(address: str, chain: str) -> bool:
    """Validate cryptocurrency address against chain-specific regex."""
    pattern = ADDRESS_PATTERNS.get(chain.lower())
    if not pattern:
        raise ValueError(f"Unsupported chain: {chain}")
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Validate numeric string for transaction amounts."""
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def validate_chain_support(chain: str) -> bool:
    """Verify chain availability in supported networks."""
    return chain.lower() in ADDRESS_PATTERNS.keys()