from decimal import Decimal, ROUND_HALF_UP
from typing import Optional

def format_crypto_amount(amount: float, decimals: int = 8) -> str:
    """Formats a crypto amount to a specific decimal precision."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    
    quantize_str = "1." + ("0" * decimals)
    result = Decimal(str(amount)).quantize(Decimal(quantize_str), rounding=ROUND_HALF_UP)
    return str(result)

def calculate_fee(amount: float, fee_rate: float) -> Decimal:
    """Calculates network transaction fee based on rate."""
    return Decimal(str(amount)) * Decimal(str(fee_rate))

def validate_address(address: str, prefix: str = '0x') -> bool:
    """Basic validation for crypto wallet addresses."""
    if not address.startswith(prefix):
        return False
    return len(address) > 26 and len(address) < 45

def convert_sats_to_btc(sats: int) -> float:
    """Converts satoshis to whole BTC."""
    return float(sats) / 100_000_000

def sanitize_input(data: str) -> str:
    """Removes whitespace and ensures lowercase for hashing."""
    return data.strip().lower()