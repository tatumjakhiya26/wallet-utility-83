import re
from typing import Union


def satoshi_to_btc(satoshis: int) -> float:
    """Convert satoshis to Bitcoin (BTC)."""
    if not isinstance(satoshis, int) or satoshis < 0:
        raise ValueError("Satoshis must be a non-negative integer.")
    return satoshis / 100_000_000


def btc_to_satoshi(btc: Union[int, float]) -> int:
    """Convert Bitcoin (BTC) to satoshis."""
    if btc < 0:
        raise ValueError("BTC amount cannot be negative.")
    return round(btc * 100_000_000)


def wei_to_eth(wei: int) -> float:
    """Convert Wei to Ethereum (ETH)."""
    if not isinstance(wei, int) or wei < 0:
        raise ValueError("Wei must be a non-negative integer.")
    return wei / 10**18


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    """Truncate a crypto wallet address for UI display."""
    if not address or len(address) <= (leading + trailing):
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def is_valid_hex_address(address: str) -> bool:
    """Check if a string matches Ethereum-style 0x hex address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))
