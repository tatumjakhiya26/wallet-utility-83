import hashlib
import re

def validate_ethereum_address(address: str) -> bool:
    """Validates if the given string is a valid Ethereum address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^(0x)?[0-9a-fA-F]{40}$", address))

def validate_bitcoin_address(address: str) -> bool:
    """Validates if the given string matches basic legacy Bitcoin address patterns."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", address))

def eth_to_wei(eth_amount: float) -> int:
    """Converts Ethereum amount to Wei."""
    return int(eth_amount * 10**18)

def wei_to_eth(wei_amount: int) -> float:
    """Converts Wei amount to Ethereum."""
    return float(wei_amount) / 10**18

def sha256_hash(data: str) -> str:
    """Returns the SHA-256 hash of the input string."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()