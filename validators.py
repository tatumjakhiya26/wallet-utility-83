import re
from typing import Optional


def is_valid_eth_address(address: str) -> bool:
    """Validate EVM/Ethereum wallet address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def is_valid_btc_address(address: str) -> bool:
    """Validate basic Legacy, P2SH, or Bech32 Bitcoin address format."""
    if not isinstance(address, str):
        return False
    btc_pattern = r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-0-9ac-hj-np-z]{8,87})$"
    return bool(re.match(btc_pattern, address))


def is_valid_tx_hash(tx_hash: str) -> bool:
    """Check if a string matches standard 32-byte hex transaction hash format."""
    if not isinstance(tx_hash, str):
        return False
    pattern = r"^(0x)?[a-fA-F0-9]{64}$"
    return bool(re.match(pattern, tx_hash))


def sanitize_address(address: str) -> Optional[str]:
    """Strip whitespaces and return normalized lower-case address if valid."""
    if not address or not isinstance(address, str):
        return None
    cleaned = address.strip()
    if is_valid_eth_address(cleaned):
        return cleaned.lower()
    if is_valid_btc_address(cleaned):
        return cleaned
    return None
