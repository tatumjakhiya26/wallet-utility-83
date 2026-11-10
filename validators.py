import re
from typing import Union

class ValidationError(Exception):
    """Raised when wallet inputs or payload values fail safety checks."""
    pass

def validate_wallet_address(address: str, chain: str = "ethereum") -> bool:
    """Validate standard crypto wallet addresses against network rules."""
    if not isinstance(address, str) or not address.strip():
        raise ValidationError("Wallet address must be a non-empty string")

    clean_address = address.strip()

    if chain.lower() == "ethereum":
        if not re.match(r"^0x[a-fA-F0-9]{40}$", clean_address):
            raise ValidationError(f"Invalid Ethereum address format: '{clean_address}'")
        return True

    elif chain.lower() in ("bitcoin", "btc"):
        btc_pattern = r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,62}$"
        if not re.match(btc_pattern, clean_address):
            raise ValidationError(f"Invalid Bitcoin address format: '{clean_address}'")
        return True

    raise ValidationError(f"Unsupported blockchain network: '{chain}'")

def validate_transaction_amount(amount_raw: Union[int, float, str], max_supply: int = 10**27) -> int:
    """Safely parse and check transaction amounts in atomic units (wei/sats)."""
    try:
        if isinstance(amount_raw, float) and not amount_raw.is_integer():
            raise ValidationError(f"Floating point loss detected for amount: {amount_raw}")
        amount = int(amount_raw)
    except (ValueError, TypeError) as err:
        raise ValidationError(f"Invalid transaction amount format: {amount_raw}") from err

    if amount <= 0:
        raise ValidationError(f"Transaction amount must be positive, got {amount}")

    if amount > max_supply:
        raise ValidationError(f"Amount {amount} exceeds safety limit {max_supply}")

    return amount
