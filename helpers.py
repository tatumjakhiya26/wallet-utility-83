"""Helper utilities for cryptocurrency formatting, conversion, and validation."""

from decimal import Decimal, ROUND_DOWN
import re
from typing import Union


def satoshi_to_btc(satoshis: int) -> Decimal:
    """Convert an amount in satoshis to Bitcoin (BTC).

    Args:
        satoshis: Integer value representing satoshis.

    Returns:
        Decimal representation of the amount in BTC.
    """
    if satoshis < 0:
        raise ValueError("Satoshi amount cannot be negative.")
    return (Decimal(satoshis) / Decimal(10**8)).quantize(Decimal("0.00000001"), rounding=ROUND_DOWN)


def btc_to_satoshi(btc_amount: Union[Decimal, float, str]) -> int:
    """Convert a Bitcoin (BTC) amount to satoshis.

    Args:
        btc_amount: Amount in BTC as Decimal, float, or string.

    Returns:
        Integer equivalent in satoshis.
    """
    decimal_amount = Decimal(str(btc_amount))
    if decimal_amount < 0:
        raise ValueError("BTC amount cannot be negative.")
    return int(decimal_amount * Decimal(10**8))


def mask_wallet_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Mask a wallet address for safe display in UI logs or screens.

    Args:
        address: Public wallet address string.
        prefix_len: Number of initial characters to keep visible.
        suffix_len: Number of trailing characters to keep visible.

    Returns:
        Truncated address with ellipsis in between.
    """
    if len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def is_hex_address(address: str) -> bool:
    """Check if a string matches basic EVM hexadecimal address structure.

    Args:
        address: Address string to validate.

    Returns:
        True if string is a valid 0x-prefixed 40-character hex address.
    """
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(pattern, address))
