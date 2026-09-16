import hashlib
import hmac
from typing import Dict, Any

def generate_signature(api_secret: str, payload: str) -> str:
    """Generates HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_currency(amount: float, precision: int = 8) -> str:
    """Formats float values for crypto precision requirements."""
    return f"{amount:.{precision}f}"

def sanitize_address(address: str) -> str:
    """Removes whitespace and ensures lowercase consistency."""
    return address.strip().lower()

def validate_transaction_fields(data: Dict[str, Any], required: list) -> bool:
    """Checks dictionary for all mandatory transaction keys."""
    return all(key in data for key in required)

def calculate_fee(amount: float, rate: float) -> float:
    """Calculates network transaction fee based on rate."""
    return round(amount * rate, 8)