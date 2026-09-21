import decimal
from typing import Union

# crypto-specific precision handling
SATOSHIS_PER_BTC = decimal.Decimal('100000000')

def format_crypto_amount(amount: Union[int, float, str], decimals: int = 8) -> str:
    """Convert raw integer satoshi units to formatted decimal string."""
    val = decimal.Decimal(str(amount))
    return f"{val / SATOSHIS_PER_BTC:.{decimals}f}"

def validate_checksum(address: str) -> bool:
    """Basic length and prefix validation for wallet addresses."""
    if not address or len(address) < 26 or len(address) > 35:
        return False
    return address[0] in ('1', '3', 'b')

def calculate_tx_fee(size_bytes: int, sat_per_byte: int) -> int:
    """Calculate total transaction fee based on market rate."""
    return size_bytes * sat_per_byte

def normalize_units(value: float, source_currency: str = 'BTC') -> decimal.Decimal:
    """Ensure all amounts are handled as high-precision decimals."""
    try:
        return decimal.Decimal(str(value)).quantize(decimal.Decimal('0.00000001'))
    except decimal.InvalidOperation:
        return decimal.Decimal('0.00000000')