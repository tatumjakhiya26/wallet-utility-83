from decimal import Decimal, ROUND_HALF_UP
from typing import Union

def format_crypto_amount(amount: Union[str, float, Decimal], decimals: int = 8) -> Decimal:
    """Normalizes crypto amounts to a fixed precision decimal."""
    val = Decimal(str(amount))
    return val.quantize(Decimal(f"1.{'0' * decimals}"), rounding=ROUND_HALF_UP)

def calculate_fee(amount: str, fee_rate: float) -> Decimal:
    """Calculates network transaction fee based on rate."""
    amount_dec = Decimal(amount)
    fee = amount_dec * Decimal(str(fee_rate))
    return fee.quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)

def validate_address_length(address: str, chain: str) -> bool:
    """Basic length check for common crypto addresses."""
    length_map = {
        'BTC': 34,
        'ETH': 42,
        'SOL': 44
    }
    expected = length_map.get(chain.upper())
    if not expected:
        return True
    return len(address) == expected