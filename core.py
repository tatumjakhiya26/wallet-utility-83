import hashlib
import secrets

def generate_wallet_key() -> str:
    """Generates a cryptographically secure hex-encoded private key."""
    return secrets.token_hex(32)

def format_wei(value: int) -> float:
    """Converts wei value to ether unit for display."""
    return value / 10**18

def validate_address(address: str) -> bool:
    """Basic validation for ethereum-style hex addresses."""
    return len(address) == 42 and address.startswith('0x')

def create_tx_hash(payload: str) -> str:
    """Creates a unique hash for transaction indexing."""
    return hashlib.sha256(payload.encode()).hexdigest()

class WalletSession:
    """Utility class for managing basic session lifecycle."""
    def __init__(self, key: str):
        self.key = key
        self.active = True

    def is_valid(self) -> bool:
        return self.active and len(self.key) == 64