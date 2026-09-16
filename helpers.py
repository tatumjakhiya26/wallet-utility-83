import re
from decimal import Decimal, InvalidOperation
from typing import Union

# Ethereum address regex (hexadecimal, 40 chars after 0x)
ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


def is_valid_eth_address(address: str) -> bool:
    """Validates if the given string is a basic Ethereum address format."""
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_PATTERN.match(address))


def truncate_address(address: str, start_chars: int = 6, end_chars: int = 4) -> str:
    """Truncates a crypto address for user interface display."""
    if not is_valid_eth_address(address):
        raise ValueError("Invalid Ethereum address format")
    return f"{address[:start_chars]}...{address[-end_chars:]}"


def eth_to_wei(eth_amount: Union[str, float, Decimal]) -> int:
    """Converts an Ethereum amount to its Wei representation."""
    try:
        decimal_amount = Decimal(str(eth_amount))
        # 1 ETH = 10^18 Wei
        return int(decimal_amount * Decimal("1000000000000000000"))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValueError(f"Invalid amount provided: {eth_amount}") from e


def wei_to_eth(wei_amount: int) -> Decimal:
    """Converts Wei representation back to Ethereum."""
    if not isinstance(wei_amount, int) or wei_amount < 0:
        raise ValueError("Wei amount must be a non-negative integer")
    return Decimal(wei_amount) / Decimal("1000000000000000000")


def format_fiat_value(amount: Union[str, float, Decimal], currency: str = "USD") -> str:
    """Formats a crypto-to-fiat conversion result safely for display."""
    try:
        val = Decimal(str(amount))
        return f"{val:,.2f} {currency.upper()}"
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValueError(f"Invalid currency amount: {amount}") from e
