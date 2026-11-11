from typing import Optional, Dict, Any
import hashlib
import hmac

def generate_signature(api_secret: str, payload: str) -> str:
    """
    Generates an HMAC-SHA256 signature for API requests.

    Args:
        api_secret: The private key for the wallet account.
        payload: The JSON-encoded request body or parameters.

    Returns:
        A hex-encoded signature string.
    """
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_currency(amount: float, precision: int = 8) -> str:
    """
    Formats float crypto amounts to standardized decimal strings.

    Args:
        amount: The numerical value to format.
        precision: The number of decimal places allowed.

    Returns:
        String representation of the amount with fixed precision.
    """
    return f"{amount:.{precision}f}"

def validate_address(address: str, chain: str = 'BTC') -> bool:
    """
    Checks if a wallet address follows expected format conventions.

    Args:
        address: The string address to validate.
        chain: The identifier for the blockchain network.

    Returns:
        Boolean indicating format validity.
    """
    if chain == 'BTC':
        return len(address) in range(26, 36) and address.isalnum()
    return len(address) == 42 and address.startswith('0x')
