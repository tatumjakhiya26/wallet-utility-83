import secrets
from decimal import Decimal
from typing import Union

SATOSHI_PER_BTC = Decimal("100000000")
WEI_PER_ETH = Decimal("1000000000000000000")


def satoshi_to_btc(satoshis: Union[int, Decimal]) -> Decimal:
    """Convert Satoshi amount to Bitcoin Decimal value."""
    return Decimal(str(satoshis)) / SATOSHI_PER_BTC


def btc_to_satoshi(btc: Union[float, str, Decimal]) -> int:
    """Convert Bitcoin amount to integer Satoshis."""
    return int(Decimal(str(btc)) * SATOSHI_PER_BTC)


def wei_to_eth(wei: Union[int, Decimal]) -> Decimal:
    """Convert Wei amount to Ether Decimal value."""
    return Decimal(str(wei)) / WEI_PER_ETH


def eth_to_wei(eth: Union[float, str, Decimal]) -> int:
    """Convert Ether amount to integer Wei."""
    return int(Decimal(str(eth)) * WEI_PER_ETH)


def format_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Format crypto address for display truncation (e.g. 0x1234...abcd)."""
    if not address or len(address) <= (prefix_len + suffix_len):
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def generate_hex_nonce(byte_length: int = 16) -> str:
    """Generate a cryptographically secure random hex string."""
    return secrets.token_hex(byte_length)
