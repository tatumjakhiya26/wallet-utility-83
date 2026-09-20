import re
from typing import Union

def wei_to_ether(wei_value: int) -> float:
    """Convert a value in Wei to its Ether equivalent.

    Args:
        wei_value: The amount in Wei to convert.

    Returns:
        The equivalent value in Ether as a float.
    """
    return wei_value / 10**18

def ether_to_wei(ether_value: Union[int, float]) -> int:
    """Convert a value in Ether to its Wei equivalent.

    Args:
        ether_value: The amount in Ether to convert.

    Returns:
        The equivalent value in Wei as an integer.
    """
    return int(ether_value * 10**18)

def is_valid_eth_address(address: str) -> bool:
    """Verify if the provided string matches the Ethereum address format.

    Args:
        address: The hexadecimal string to validate.

    Returns:
        True if the address is valid, False otherwise.
    """
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))

def truncate_address(address: str, start_chars: int = 6, end_chars: int = 4) -> str:
    """Truncate a crypto address for display purposes.

    Args:
        address: The full wallet address.
        start_chars: Number of characters to keep at the beginning.
        end_chars: Number of characters to keep at the end.

    Returns:
        The truncated address with ellipses (e.g., '0x1234...abcd').
    """
    if len(address) <= (start_chars + end_chars + 3):
        return address
    return f"{address[:start_chars]}...{address[-end_chars:]}"
