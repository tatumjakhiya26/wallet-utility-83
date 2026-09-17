import re


def btc_to_satoshi(btc_amount: float) -> int:
    """Convert Bitcoin amount to Satoshi unit."""
    if btc_amount < 0:
        raise ValueError("Amount cannot be negative")
    return int(round(btc_amount * 100_000_000))


def satoshi_to_btc(satoshi_amount: int) -> float:
    """Convert Satoshi unit to Bitcoin amount."""
    if satoshi_amount < 0:
        raise ValueError("Amount cannot be negative")
    return float(satoshi_amount) / 100_000_000


def is_valid_eth_address(address: str) -> bool:
    """Verify if the string matches basic Ethereum address structure."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def truncate_address(address: str, start_chars: int = 6, end_chars: int = 4) -> str:
    """Truncate a crypto address for safe UI visualization."""
    if not address or len(address) <= (start_chars + end_chars):
        return address
    return f"{address[:start_chars]}...{address[-end_chars:]}"
