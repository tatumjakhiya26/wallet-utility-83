import decimal
from typing import Union

# Set precision for crypto calculations
DECIMAL_CONTEXT = decimal.Context(prec=28, rounding=decimal.ROUND_HALF_UP)

def to_base_unit(amount: Union[int, float, str], decimals: int = 18) -> int:
    """Converts human-readable crypto amount to base atomic units."""
    val = decimal.Decimal(str(amount))
    multiplier = decimal.Decimal(10) ** decimals
    return int((val * multiplier).to_integral_value())

def from_base_unit(amount: int, decimals: int = 18) -> decimal.Decimal:
    """Converts atomic units back to decimal format."""
    val = decimal.Decimal(amount)
    divisor = decimal.Decimal(10) ** decimals
    return val / divisor

def format_crypto(amount: decimal.Decimal, precision: int = 8) -> str:
    """Formats decimal objects for display purposes."""
    template = f"{{:.{precision}f}}"
    return template.format(amount.normalize())

def validate_address(address: str, prefix: str = '0x', length: int = 42) -> bool:
    """Basic validation for crypto wallet address strings."""
    if not address.startswith(prefix):
        return False
    if len(address) != length:
        return False
    return address[len(prefix):].isalnum()