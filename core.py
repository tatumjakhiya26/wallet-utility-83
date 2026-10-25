from decimal import Decimal, ROUND_HALF_UP
from typing import Optional

def format_crypto_amount(amount: str, decimals: int = 8) -> str:
    """Standardizes crypto values to specified precision."""
    try:
        value = Decimal(amount)
        quantizer = Decimal('1.' + '0' * decimals)
        return str(value.quantize(quantizer, rounding=ROUND_HALF_UP))
    except (ValueError, TypeError):
        return "0.00000000"

def validate_address(address: str, chain: str) -> bool:
    """Basic length and prefix validation for wallets."""
    rules = {
        "btc": (lambda a: len(a) in [26, 34, 42, 62] and a.isalnum()),
        "eth": (lambda a: len(a) == 42 and a.startswith("0x"))
    }
    validator = rules.get(chain.lower())
    return validator(address) if validator else False

def calculate_fee(amount: str, rate: float) -> str:
    """Transaction fee calculation based on network rate."""
    amount_dec = Decimal(amount)
    fee = amount_dec * Decimal(str(rate))
    return str(fee.quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP))