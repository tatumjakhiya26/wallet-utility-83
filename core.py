import hashlib
import secrets

def generate_wallet_key() -> str:
    """Generates a cryptographically secure hex wallet key."""
    return secrets.token_hex(32)

def format_wei_to_eth(wei: int) -> float:
    """Converts raw wei units to readable ether format."""
    return wei / 10**18

def calculate_tx_hash(data: str) -> str:
    """Creates a SHA-256 hash for transaction tracking."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def validate_address_format(address: str) -> bool:
    """Checks basic ethereum-style address integrity."""
    if not address.startswith('0x') or len(address) != 42:
        return False
    return all(c in '0123456789abcdefABCDEF' for c in address[2:])

class WalletSession:
    """Container for active wallet state operations."""
    def __init__(self, wallet_id: str):
        self.wallet_id = wallet_id
        self.is_active = True

    def get_status_summary(self) -> dict:
        return {
            "id": self.wallet_id,
            "active": self.is_active
        }