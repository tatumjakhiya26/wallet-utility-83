from decimal import Decimal, ROUND_HALF_UP
from typing import Optional

def format_crypto_amount(amount: str, decimals: int = 8) -> str:
    """Normalizes crypto amount strings to fixed decimal precision."""
    try:
        value = Decimal(amount)
        quantizer = Decimal('1.' + '0' * decimals)
        return str(value.quantize(quantizer, rounding=ROUND_HALF_UP))
    except (ValueError, ArithmeticError):
        return "0.00000000"

def validate_address_format(address: str, chain: str) -> bool:
    """Checks basic address patterns for supported chains."""
    patterns = {
        "eth": lambda a: len(a) == 42 and a.startswith("0x"),
        "btc": lambda a: len(a) in range(26, 36) and a[0] in ("1", "3", "b")
    }
    validator = patterns.get(chain.lower())
    return validator(address) if validator else False

def calculate_transaction_fee(amount: str, fee_rate: float) -> str:
    """Calculates fee based on amount and rate percentage."""
    try:
        fee = Decimal(amount) * Decimal(str(fee_rate))
        return format_crypto_amount(str(fee))
    except (ValueError, TypeError):
        return "0.00000000"