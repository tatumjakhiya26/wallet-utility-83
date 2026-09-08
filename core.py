import hashlib
import binascii
from typing import Union

class CryptographicWallet:
    """A utility class providing basic cryptographic tools for wallet operations."""

    def __init__(self, coin_symbol: str) -> None:
        """Initializes the wallet utility for a specific coin symbol."""
        self.coin_symbol = coin_symbol.upper()

    def generate_sha256(self, data: bytes) -> str:
        """Generates a SHA-256 hex string from the input bytes."""
        return hashlib.sha256(data).hexdigest()

    def validate_private_key(self, private_key_hex: str) -> bool:
        """Validates if a given hex string represents a valid 256-bit private key."""
        if len(private_key_hex) != 64:
            return False
        try:
            val = int(private_key_hex, 16)
            return 0 < val < 115792089237316195423570985008687907852837564279074904382605163141518161494337
        except ValueError:
            return False

    def derive_mock_address(self, public_key_hex: str) -> str:
        """Derives a mock wallet address from a public key string."""
        if not public_key_hex:
            raise ValueError("Public key cannot be empty")
        try:
            pub_bytes = binascii.unhexlify(public_key_hex)
            hashed = hashlib.sha256(pub_bytes).hexdigest()
            suffix = hashed[-40:]
            if self.coin_symbol == "ETH":
                return f"0x{suffix}"
            return f"1{suffix[:33]}"
        except (ValueError, binascii.Error) as err:
            raise ValueError(f"Invalid public key format: {err}")