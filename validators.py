import re
from typing import Optional

def validate_bitcoin_address(address: str) -> bool:
    """Validate Bitcoin address format using regex.

    Args:
        address: The BTC address string to verify.

    Returns:
        bool: True if address is valid, False otherwise.
    """
    btc_pattern: str = r'^(1|3|bc1)[a-zA-Z0-9]{25,59}$'
    return bool(re.match(btc_pattern, address))

def validate_ethereum_address(address: str) -> bool:
    """Validate Ethereum address format.

    Args:
        address: The ETH address string to verify.

    Returns:
        bool: True if address is valid, False otherwise.
    """
    eth_pattern: str = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(eth_pattern, address))

def sanitize_amount(amount: str) -> Optional[float]:
    """Convert string amount to float safely.

    Args:
        amount: Numeric string representation.

    Returns:
        float value if valid, None if conversion fails.
    """
    try:
        value: float = float(amount)
        return value if value >= 0 else None
    except (ValueError, TypeError):
        return None