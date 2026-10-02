from decimal import Decimal
from typing import Optional, Union


def format_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Truncates a cryptocurrency address for UI display.

    Args:
        address: The full wallet address string.
        prefix_len: Number of characters to retain at the start.
        suffix_len: Number of characters to retain at the end.

    Returns:
        A shortened address string formatted like '0x1234...abcd'.
    """
    if not address or len(address) <= (prefix_len + suffix_len):
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def convert_to_base_unit(
    value: Union[int, float, str, Decimal], decimals: int = 18
) -> Decimal:
    """Converts a raw token amount to base unit (e.g., Wei to ETH).

    Args:
        value: Amount in smallest unit (e.g., Wei or Satoshi).
        decimals: Number of decimal places for the token or coin.

    Returns:
        Decimal representation of the amount in base units.
    """
    decimal_val = Decimal(str(value))
    factor = Decimal(10) ** decimals
    return decimal_val / factor


def is_valid_hex_address(address: str, expected_length: Optional[int] = 42) -> bool:
    """Validates whether a string is a valid hex-encoded crypto address.

    Args:
        address: The wallet address string to check.
        expected_length: Expected total character length including '0x'.

    Returns:
        True if the address is a valid hex string, False otherwise.
    """
    if not address.startswith("0x"):
        return False
    if expected_length is not None and len(address) != expected_length:
        return False

    try:
        int(address[2:], 16)
        return True
    except ValueError:
        return False
