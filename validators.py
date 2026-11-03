import re
from typing import Optional

def validate_ethereum_address(address: str) -> bool:
    """Verify valid ethereum hex address format."""
    if not isinstance(address, str):
        return False
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """Validate numeric amount string for transaction safety."""
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def format_wei_to_eth(wei_value: int) -> float:
    """Convert wei integer to human-readable eth float."""
    if not isinstance(wei_value, int) or wei_value < 0:
        return 0.0
    return float(wei_value) / 10**18

def sanitize_memo(memo: Optional[str]) -> str:
    """Clean memo string to prevent injection issues."""
    if not memo:
        return ""
    # Allow alphanumeric and common punctuation, remove others
    clean = re.sub(r'[^a-zA-Z0-9\s\-_]', '', memo)
    return clean[:128].strip()