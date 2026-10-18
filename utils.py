import re
from decimal import Decimal, InvalidOperation
from typing import Union


class CryptoValidationError(Exception):
    """Custom exception raised when crypto validation fails."""
    pass


def wei_to_ether(wei_value: Union[int, str, float]) -> Decimal:
    """Convert Wei amount to Ether handling numeric precision edge cases."""
    try:
        str_val = str(wei_value).strip()
        if not str_val:
            raise CryptoValidationError("Wei amount cannot be empty")
        
        val = Decimal(str_val)
        if val < 0:
            raise CryptoValidationError("Wei amount cannot be negative")
        
        return val / Decimal("1000000000000000000")
    except (InvalidOperation, ValueError) as err:
        raise CryptoValidationError(f"Invalid Wei string representation: '{wei_value}'") from err


def validate_hex_address(address: str, expected_prefix: str = "0x") -> str:
    """Validate and normalize hex wallet address edge cases."""
    if not isinstance(address, str):
        raise CryptoValidationError("Address must be a string")

    clean_addr = address.strip()
    if not clean_addr:
        raise CryptoValidationError("Address cannot be empty or whitespace")

    if expected_prefix and not clean_addr.startswith(expected_prefix):
        raise CryptoValidationError(f"Address must start with '{expected_prefix}'")

    hex_part = clean_addr[len(expected_prefix):]
    if len(hex_part) != 40:
        raise CryptoValidationError(f"Invalid hex body length: expected 40, got {len(hex_part)}")

    if not re.fullmatch(r"[0-9a-fA-F]{40}", hex_part):
        raise CryptoValidationError("Address contains invalid non-hexadecimal characters")

    return clean_addr.lower()


def safe_format_tx_hash(tx_hash: str, start_chars: int = 6, end_chars: int = 4) -> str:
    """Safely truncate transaction hash for UI display without throwing exceptions."""
    if not isinstance(tx_hash, str) or not tx_hash.strip():
        return "0x..."
    
    cleaned = tx_hash.strip()
    min_length = start_chars + end_chars + 3
    if len(cleaned) < min_length:
        return cleaned

    return f"{cleaned[:start_chars]}...{cleaned[-end_chars:]}"