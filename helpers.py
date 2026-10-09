import decimal
from typing import Union

def format_sats(amount: Union[int, float, str]) -> decimal.Decimal:
    """Converts raw satoshi values to standard BTC format."""
    return decimal.Decimal(amount) / decimal.Decimal(10**8)

def validate_address(address: str) -> bool:
    """Basic length check for crypto wallet addresses."""
    return 26 <= len(address) <= 35

def calculate_fee(gas_price: int, gas_limit: int) -> int:
    """Calculates total transaction fee in wei/sats."""
    return int(gas_price * gas_limit)

def wei_to_ether(wei: int) -> float:
    """Converts wei units to ether float value."""
    return float(wei) / 10**18

def mask_address(address: str) -> str:
    """Masks sensitive address string for logging."""
    if len(address) < 10:
        return "****"
    return f"{address[:6]}...{address[-4:]}"