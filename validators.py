import re
from typing import Optional

def validate_bitcoin_address(address: str) -> bool:
    """
    Validates a Bitcoin address format using regex.

    Args:
        address: The string address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$'
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """
    Checks if a numeric string is a valid positive decimal.

    Args:
        amount: The string representation of the crypto amount.

    Returns:
        bool: True if strictly positive numeric value.
    """
    try:
        value = float(amount)
        return value > 0
    except ValueError:
        return False

def sanitize_memo(memo: Optional[str]) -> str:
    """
    Ensures the memo field contains only alphanumeric characters.

    Args:
        memo: The optional transaction memo.

    Returns:
        str: Sanitized string safe for network broadcast.
    """
    if not memo:
        return ""
    return re.sub(r'[^a-zA-Z0-9]', '', memo)