from typing import Dict, Any, Optional
import decimal

def format_crypto_amount(amount: str, precision: int = 8) -> str:
    """Converts raw string amount to standardized decimal format."""
    try:
        d = decimal.Decimal(amount)
        return format(d, f'.{precision}f').rstrip('0').rstrip('.')
    except (decimal.InvalidOperation, ValueError):
        return "0.0"

def sanitize_address(address: str) -> str:
    """Removes whitespace and forces lowercase for address consistency."""
    return address.strip().lower()

def calculate_fee(amount: str, rate: float) -> str:
    """Calculates transaction fee based on provided percentage rate."""
    try:
        fee = decimal.Decimal(amount) * decimal.Decimal(str(rate))
        return str(fee.quantize(decimal.Decimal('0.00000001')))
    except Exception:
        return "0.00000000"

def validate_tx_data(data: Dict[str, Any]) -> bool:
    """Checks for presence of required transaction keys."""
    required = {'from', 'to', 'value', 'currency'}
    return all(key in data for key in required)