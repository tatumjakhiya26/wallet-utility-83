import hashlib
import os
from typing import Optional

def generate_address_checksum(address: str) -> str:
    """Generates a checksum for EIP-55 compatibility."""
    address = address.lower().replace("0x", "")
    hash_result = hashlib.sha3_256(address.encode()).hexdigest()
    checksum = "0x"
    for i in range(len(address)):
        if int(hash_result[i], 16) >= 8:
            checksum += address[i].upper()
        else:
            checksum += address[i]
    return checksum

def validate_mnemonic(mnemonic: str) -> bool:
    """Checks if a 12 or 24 word mnemonic phrase is valid."""
    words = mnemonic.strip().split()
    return len(words) in [12, 24]

def secure_random_bytes(length: int = 32) -> bytes:
    """Generates cryptographically secure random bytes."""
    return os.urandom(length)

def format_wei_to_eth(wei: int) -> float:
    """Converts wei unit to human-readable eth."""
    return wei / 10**18

def sanitize_address(address: str) -> str:
    """Ensures address is lowercase with 0x prefix."""
    clean = address.lower().strip()
    return clean if clean.startswith("0x") else f"0x{clean}"