from decimal import Decimal, InvalidOperation
from typing import Optional

def normalize_amount(amount: str, precision: int = 8) -> Optional[Decimal]:
    """Converts raw string input to a normalized Decimal for calculations."""
    try:
        value = Decimal(amount)
        if value < 0:
            return None
        return value.quantize(Decimal('1.' + '0' * precision))
    except (InvalidOperation, ValueError, TypeError):
        return None

def format_crypto_address(address: str) -> str:
    """Sanitizes and formats blockchain address string."""
    clean_address = address.strip().lower()
    if not clean_address.startswith('0x'):
        return f'0x{clean_address}'
    return clean_address

def calculate_fee(amount: Decimal, rate: str) -> Decimal:
    """Calculates network transaction fee based on percentage rate."""
    fee_rate = Decimal(rate)
    return (amount * fee_rate).quantize(Decimal('0.00000001'))

def validate_transaction_payload(payload: dict) -> bool:
    """Ensures all required fields exist in wallet transaction."""
    required = ['sender', 'receiver', 'amount', 'currency']
    return all(key in payload for key in required)