import re
from typing import Optional

# crypto address validation patterns
ADDRESS_PATTERNS = {
    'BTC': r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$',
    'ETH': r'^0x[a-fA-F0-9]{40}$'
}

class AddressValidator:
    """Utility class for verifying crypto wallet address formats."""
    
    @staticmethod
    def validate(address: str, chain: str) -> bool:
        """Checks if provided address matches the chain regex."""
        pattern = ADDRESS_PATTERNS.get(chain.upper())
        if not pattern:
            return False
        return bool(re.match(pattern, address))

    @staticmethod
    def sanitize_input(data: str) -> str:
        """Removes whitespace and ensures lowercase for hex addresses."""
        cleaned = data.strip()
        if cleaned.startswith('0x'):
            return cleaned.lower()
        return cleaned

def is_valid_private_key(key: str) -> bool:
    """Simple check for hex private key character range."""
    return bool(re.match(r'^[a-fA-F0-9]{64}$', key))