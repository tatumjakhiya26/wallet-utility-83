import re
from typing import Dict, Any

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
BTC_ADDRESS_PATTERN = re.compile(r"^(1|3|[a-km-zA-HJ-NP-Z1-9]{26,35}|bc1[a-z0-9]{39,59})$")


def is_valid_eth_address(address: str) -> bool:
    """Validate if a string matches standard Ethereum address format.

    Args:
        address: Hexadecimal string representing the Ethereum address.

    Returns:
        True if valid format, False otherwise.
    """
    if not address or not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_PATTERN.match(address))


def is_valid_btc_address(address: str) -> bool:
    """Validate Bitcoin address format for Legacy, P2SH, or Bech32.

    Args:
        address: String representing the Bitcoin recipient address.

    Returns:
        True if address matches Bitcoin formats, False otherwise.
    """
    if not address or not isinstance(address, str):
        return False
    return bool(BTC_ADDRESS_PATTERN.match(address))


def validate_transaction_payload(payload: Dict[str, Any]) -> bool:
    """Ensure transaction payload contains required fields and valid amounts.

    Args:
        payload: Dictionary containing 'sender', 'recipient', and 'amount'.

    Returns:
        True if payload is structurally sound, False otherwise.
    """
    required_keys = {"sender", "recipient", "amount"}
    if not required_keys.issubset(payload.keys()):
        return False

    amount = payload.get("amount")
    if not isinstance(amount, (int, float)) or amount <= 0:
        return False

    return True
