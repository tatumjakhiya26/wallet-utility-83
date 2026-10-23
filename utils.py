from decimal import Decimal, ROUND_HALF_UP
from typing import Union

def format_crypto_amount(amount: Union[str, float, Decimal], decimals: int = 8) -> str:
    """Normalizes crypto amount string for precision consistency."""
    try:
        d_amount = Decimal(str(amount))
        quantizer = Decimal('1.' + '0' * decimals)
        return str(d_amount.quantize(quantizer, rounding=ROUND_HALF_UP))
    except (ValueError, ArithmeticError):
        return "0.00000000"

def calculate_fee(amount: str, fee_rate: float) -> str:
    """Calculates transaction fee based on percentage rate."""
    amount_dec = Decimal(amount)
    fee = amount_dec * Decimal(str(fee_rate))
    return format_crypto_amount(fee)

def validate_address_format(address: str, chain: str) -> bool:
    """Validates address length based on network chain."""
    # Basic length check for common EVM/BTC patterns
    chain_rules = {
        "eth": 42,  # 0x + 40 hex
        "btc": 34   # Legacy address range
    }
    expected_len = chain_rules.get(chain.lower())
    return len(address) == expected_len if expected_len else False