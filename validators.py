import re
from typing import Optional


class ValidationError(Exception):
    """Raised when a crypto validation check fails."""
    pass


def is_hex_string(val: str, expected_len: Optional[int] = None) -> bool:
    """Check if string is valid hex with optional length check."""
    if not isinstance(val, str):
        return False
    clean_val = val[2:] if val.startswith("0x") else val
    if expected_len and len(clean_val) != expected_len:
        return False
    return bool(re.fullmatch(r"^[0-9a-fA-F]+$", clean_val))


def validate_eth_address(address: str) -> str:
    """Validate Ethereum address format and return normalized address."""
    if not isinstance(address, str):
        raise ValidationError("Address must be a string")
    if not re.fullmatch(r"^0x[0-9a-fA-F]{40}$", address):
        raise ValidationError(f"Invalid Ethereum address format: {address}")
    return address.lower()


def validate_btc_address(address: str) -> bool:
    """Validate legacy (P2PKH/P2SH) or Bech32 Bitcoin address format."""
    if not isinstance(address, str):
        return False
    legacy_pattern = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    bech32_pattern = r"^bc1[a-0-9ac-hj-np-z]{8,87}$"
    return bool(re.fullmatch(legacy_pattern, address) or re.fullmatch(bech32_pattern, address, re.IGNORECASE))


def validate_tx_hash(tx_hash: str) -> bool:
    """Validate 32-byte transaction hash represented as 64 hex chars."""
    return is_hex_string(tx_hash, expected_len=64)
