import hashlib
import re
import secrets

ETH_ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')


def wei_to_ether(wei: int) -> float:
    """Convert Wei to Ether."""
    if not isinstance(wei, int) or wei < 0:
        raise ValueError('Wei value must be a non-negative integer.')
    return wei / (10 ** 18)


def ether_to_wei(ether: float) -> int:
    """Convert Ether to Wei."""
    if not isinstance(ether, (int, float)) or ether < 0:
        raise ValueError('Ether value must be a non-negative number.')
    return int(ether * (10 ** 18))


def is_valid_eth_address(address: str) -> bool:
    """Check if the given string is a valid Ethereum address format."""
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_PATTERN.match(address))


def generate_private_key() -> str:
    """Generate a secure 256-bit private key represented as a hex string."""
    return secrets.token_hex(32)


def derive_mock_address(private_key_hex: str) -> str:
    """Derive a mock wallet address from a private key using SHA-256."""
    if len(private_key_hex) != 64:
        raise ValueError('Invalid private key length.')
    try:
        private_bytes = bytes.fromhex(private_key_hex)
    except ValueError:
        raise ValueError('Private key must be a valid hex string.')
    
    hash_bytes = hashlib.sha256(private_bytes).digest()
    address_bytes = hashlib.sha256(hash_bytes).digest()[-20:]
    return '0x' + address_bytes.hex()