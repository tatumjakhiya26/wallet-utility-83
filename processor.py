from decimal import Decimal, ROUND_HALF_UP
from typing import Optional

def format_crypto_amount(amount: str, decimals: int = 8) -> Decimal:
    """Converts string amount to Decimal with specified precision."""
    return Decimal(amount).quantize(Decimal(10)**-decimals, rounding=ROUND_HALF_UP)

def calculate_fee(amount: Decimal, fee_rate: float) -> Decimal:
    """Calculates network fee based on percentage rate."""
    fee = amount * Decimal(str(fee_rate))
    return fee.quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)

def validate_address_format(address: str, prefix: str = '0x') -> bool:
    """Basic validation for crypto address string format."""
    if not address.startswith(prefix):
        return False
    return len(address) == 42

def mask_address(address: str) -> str:
    """Redacts middle of address for log safety."""
    if len(address) < 10:
        return "****"
    return f"{address[:6]}...{address[-4:]}"

def calculate_net_amount(amount: Decimal, fee: Decimal) -> Decimal:
    """Subtracts fee from total transaction amount."""
    return (amount - fee).max(Decimal('0'))