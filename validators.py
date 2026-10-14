import re

class AddressValidationError(Exception):
    """Custom exception for crypto address validation issues."""
    pass

def validate_wallet_address(address: str, chain_type: str = 'evm') -> bool:
    """Validates address format based on network type."""
    if not isinstance(address, str):
        raise AddressValidationError("Address must be a string.")
    
    if not address:
        raise AddressValidationError("Address cannot be empty.")

    if chain_type == 'evm':
        # Standard Ethereum address regex: 0x followed by 40 hex chars
        if not re.match(r'^0x[a-fA-F0-9]{40}$', address):
            raise AddressValidationError(f"Invalid EVM address format: {address}")
        return True
    
    if chain_type == 'solana':
        # Solana addresses are base58, 32-44 characters
        if not re.match(r'^[1-9A-HJ-NP-Za-km-z]{32,44}$', address):
            raise AddressValidationError(f"Invalid Solana address format: {address}")
        return True

    raise ValueError(f"Unsupported chain type: {chain_type}")

def sanitize_input(data: str) -> str:
    """Removes potential shell/injection characters from user input."""
    if not data:
        return ""
    return re.sub(r'[^a-zA-Z0-9]', '', data)