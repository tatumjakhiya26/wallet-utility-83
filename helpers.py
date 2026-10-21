from typing import Union, Optional

def format_address(address: str) -> str:
    """Shorten crypto address for display."""
    if len(address) < 10:
        return address
    return f"{address[:6]}...{address[-4:]}"

def to_wei(amount: Union[int, float], decimals: int = 18) -> int:
    """Convert human-readable currency to wei units."""
    return int(amount * (10 ** decimals))

def validate_transaction_hash(tx_hash: str) -> bool:
    """Verify basic hexadecimal transaction hash format."""
    if not tx_hash.startswith("0x"):
        return False
    return len(tx_hash) == 66 and all(c in "0123456789abcdefABCDEF" for c in tx_hash[2:])

def calculate_fee(gas_price: int, gas_limit: int) -> int:
    """Calculate total transaction cost in wei."""
    return gas_price * gas_limit

def sanitize_input(value: Optional[str]) -> str:
    """Normalize string input for crypto operations."""
    if value is None:
        return ""
    return value.strip().lower()