import hashlib
import hmac
from decimal import Decimal

def format_crypto_amount(amount: float, precision: int = 8) -> Decimal:
    """Converts float amount to high-precision Decimal."""
    return Decimal(str(amount)).quantize(Decimal(f"1.{'0' * precision}"))

def generate_signature(api_secret: str, payload: str) -> str:
    """Creates HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def validate_address_format(address: str, prefix: str = '0x') -> bool:
    """Checks basic crypto address structure."""
    if not address or not address.startswith(prefix):
        return False
    return len(address) == 42

def calculate_fee(amount: Decimal, fee_rate: float) -> Decimal:
    """Computes transaction fee based on rate."""
    return (amount * Decimal(str(fee_rate))).quantize(Decimal('0.00000001'))