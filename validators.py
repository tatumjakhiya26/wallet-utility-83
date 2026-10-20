import re

class WalletValidationError(Exception):
    """Custom exception for crypto address validation issues."""
    pass

def validate_address(address: str, chain_type: str = "eth") -> bool:
    """
    Validates crypto addresses based on network patterns.
    Returns True if valid, otherwise raises WalletValidationError.
    """
    patterns = {
        "eth": r"^0x[a-fA-F0-9]{40}$",
        "btc": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    }

    if chain_type not in patterns:
        raise WalletValidationError(f"Unsupported chain type: {chain_type}")

    if not re.match(patterns[chain_type], address):
        raise WalletValidationError(f"Invalid {chain_type} address format")

    return True

def validate_amount(amount: float) -> bool:
    """
    Ensures the transaction amount is positive and within logical bounds.
    """
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise WalletValidationError("Transaction amount must be a positive number")
    
    if amount > 1_000_000:
        raise WalletValidationError("Transaction amount exceeds single transfer limit")

    return True