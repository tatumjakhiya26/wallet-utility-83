from typing import List, Optional, Union
from decimal import Decimal

def format_crypto_amount(amount: Union[str, float, Decimal], decimals: int = 8) -> str:
    """
    Formats crypto amounts to a fixed decimal precision string.

    Args:
        amount: The numeric value to format.
        decimals: Number of decimal places to include.

    Returns:
        A string representation of the formatted amount.
    """
    value = Decimal(str(amount))
    return f"{value:.{decimals}f}"

def validate_address(address: str, chain: str) -> bool:
    """
    Checks if the provided string is a valid address for the given chain.

    Args:
        address: The wallet address string.
        chain: The identifier for the blockchain (e.g., 'BTC', 'ETH').

    Returns:
        Boolean indicating validity.
    """
    if not address or len(address) < 26:
        return False

    if chain == 'BTC':
        return address.startswith(('1', '3', 'bc1'))
    elif chain == 'ETH':
        return address.startswith('0x') and len(address) == 42
    
    return False

def calculate_fee(amount: Decimal, rate: float) -> Decimal:
    """
    Computes transaction fee based on amount and network rate.

    Args:
        amount: The total amount in the transaction.
        rate: The fee rate multiplier.

    Returns:
        The calculated fee as a Decimal object.
    """
    return amount * Decimal(str(rate))