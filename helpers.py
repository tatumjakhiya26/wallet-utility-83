import decimal
from typing import Optional

# Decimal precision standards for major cryptocurrencies
ETH_DECIMALS = 18
BTC_DECIMALS = 8


def wei_to_eth(wei_value: int) -> decimal.Decimal:
    """Convert Wei integer amount to ETH Decimal."""
    if wei_value < 0:
        raise ValueError("Amount cannot be negative")
    return decimal.Decimal(wei_value) / decimal.Decimal(10**ETH_DECIMALS)


def eth_to_wei(eth_value: float | decimal.Decimal) -> int:
    """Convert ETH amount to Wei integer precision."""
    amount = decimal.Decimal(str(eth_value))
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return int(amount * decimal.Decimal(10**ETH_DECIMALS))


def shorten_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Format crypto address for UI display (e.g., 0x1234...abcd)."""
    if not address or len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def calculate_gas_fee(gas_limit: int, gas_price_gwei: float) -> decimal.Decimal:
    """Calculate total transaction gas fee in ETH given gas limit and Gwei price."""
    gwei_decimal = decimal.Decimal(str(gas_price_gwei))
    eth_per_gwei = decimal.Decimal("1e-9")
    return decimal.Decimal(gas_limit) * gwei_decimal * eth_per_gwei


def get_explorer_url(address: str, chain: str = "ethereum") -> Optional[str]:
    """Generate block explorer URL for a wallet address on supported chains."""
    explorers = {
        "ethereum": f"https://etherscan.io/address/{address}",
        "polygon": f"https://polygonscan.com/address/{address}",
        "bsc": f"https://bscscan.com/address/{address}",
        "bitcoin": f"https://mempool.space/address/{address}",
    }
    return explorers.get(chain.lower())
