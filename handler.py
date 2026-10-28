import hashlib
import os
import json

def generate_address_checksum(public_key: str) -> str:
    """Generates a simple hex checksum for a given public key string."""
    hash_obj = hashlib.sha256(public_key.encode())
    return hash_obj.hexdigest()[:8]

def validate_payload_integrity(data: dict, checksum: str) -> bool:
    """Verifies dictionary data against a provided checksum string."""
    serialized = json.dumps(data, sort_keys=True)
    expected = hashlib.sha256(serialized.encode()).hexdigest()[:8]
    return expected == checksum

def format_wei_to_eth(wei_value: int) -> float:
    """Converts raw wei integers to standard ether float representation."""
    return float(wei_value) / 10**18

def get_environment_config(key: str, default: str = None) -> str:
    """Retrieves environment configuration with fallback logic."""
    return os.getenv(key, default)

def sanitize_wallet_label(label: str) -> str:
    """Cleans wallet label input to alphanumeric characters only."""
    return "".join(char for char in label if char.isalnum())