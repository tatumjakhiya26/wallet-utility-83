import hashlib
import os
from typing import Optional

def validate_address(address: str, prefix: str = '0x') -> bool:
    """Checks if a crypto address matches expected hex format."""
    if not address.startswith(prefix):
        return False
    return len(address) == 42 and all(c in '0123456789abcdefABCDEF' for c in address[2:])

def generate_nonce(length: int = 32) -> str:
    """Creates a secure random string for API requests."""
    return os.urandom(length).hex()

def format_wei_to_eth(wei: int) -> float:
    """Converts raw wei units to readable ether format."""
    return wei / 10**18

def calculate_checksum(data: str) -> str:
    """Generates a SHA-256 hash for data integrity verification."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def parse_env_float(value: Optional[str], default: float = 0.0) -> float:
    """Safe conversion of environment strings to floats."""
    try:
        return float(value) if value else default
    except (TypeError, ValueError):
        return default