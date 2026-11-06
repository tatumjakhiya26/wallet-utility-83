import re
from decimal import Decimal, ROUND_HALF_UP

SATOSHI_PER_BTC = 100_000_000
WEI_PER_ETH = 10**18


def satoshi_to_btc(satoshis: int) -> Decimal:
    """Convert satoshis to BTC decimal value."""
    if satoshis < 0:
        raise ValueError("Satoshi value cannot be negative")
    return (Decimal(satoshis) / Decimal(SATOSHI_PER_BTC)).quantize(
        Decimal("0.00000001")
    )


def wei_to_eth(wei: int) -> Decimal:
    """Convert Wei to ETH decimal value."""
    if wei < 0:
        raise ValueError("Wei value cannot be negative")
    return Decimal(wei) / Decimal(WEI_PER_ETH)


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Truncate a crypto address for UI display."""
    if not address or len(address) <= (prefix_len + suffix_len):
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def is_valid_eth_address(address: str) -> bool:
    """Check if string matches standard Ethereum hexadecimal address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def format_fiat_amount(amount: float, symbol: str = "$") -> str:
    """Format numerical amount as standard currency string."""
    decimal_val = Decimal(str(amount)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    return f"{symbol}{decimal_val:,.2f}"
