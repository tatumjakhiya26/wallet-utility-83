from typing import Dict, Union, Optional
from decimal import Decimal, ROUND_HALF_UP

def format_crypto_amount(amount: Union[str, float, Decimal], precision: int = 8) -> str:
    """Normalizes crypto amounts to a fixed precision string."""
    try:
        d_amount = Decimal(str(amount))
        return f"{d_amount.quantize(Decimal('1.' + '0' * precision), rounding=ROUND_HALF_UP):f}"
    except Exception:
        return "0.00000000"

def sanitize_address(address: str) -> str:
    """Removes whitespace and ensures consistent checksum casing."""
    if not address:
        return ""
    return address.strip().lower()

def calculate_fee(amount: Decimal, rate: float) -> Decimal:
    """Computes transaction fee based on percentage rate."""
    fee = amount * Decimal(str(rate))
    return fee.quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)

def validate_transaction_data(data: Dict) -> bool:
    """Basic structure validation for incoming transaction payloads."""
    required_fields = {'sender', 'receiver', 'amount', 'asset'}
    return all(field in data for field in required_fields)