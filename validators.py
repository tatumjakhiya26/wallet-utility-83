import re

class WalletValidationError(Exception):
    """Custom exception for crypto wallet validation failures."""
    pass

def validate_address(address: str, chain: str) -> bool:
    """
    Validates wallet addresses based on blockchain patterns.
    Raises WalletValidationError for malformed inputs.
    """
    if not address or not isinstance(address, str):
        raise WalletValidationError("Address must be a non-empty string")

    patterns = {
        "ETH": r"^0x[a-fA-F0-9]{40}$",
        "BTC": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    }

    if chain not in patterns:
        raise ValueError(f"Unsupported chain: {chain}")

    if not re.match(patterns[chain], address):
        raise WalletValidationError(f"Invalid {chain} address format")

    return True

def sanitize_amount(amount: str) -> float:
    """
    Parses and sanitizes numeric strings for financial operations.
    """
    try:
        value = float(amount)
        if value < 0:
            raise WalletValidationError("Amount cannot be negative")
        return value
    except (ValueError, TypeError):
        raise WalletValidationError("Invalid numeric format for amount")