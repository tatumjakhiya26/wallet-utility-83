from decimal import Decimal, DecimalException, InvalidOperation
import re
from typing import Optional

ETH_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
BTC_ADDRESS_REGEX = re.compile(r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,62}$")
HEX_32BYTES_REGEX = re.compile(r"^0x[a-fA-F0-9]{64}$")


def validate_wallet_address(address: str, chain: str = "ETH") -> bool:
    """Validate cryptocurrency address formats with strict type and edge case checks."""
    if not isinstance(address, str) or not address.strip():
        return False

    clean_addr = address.strip()

    # Check for invalid control characters or null bytes in input
    if "\x00" in clean_addr or any(ord(c) < 32 for c in clean_addr):
        return False

    chain_upper = chain.upper()
    if chain_upper == "ETH":
        return bool(ETH_ADDRESS_REGEX.match(clean_addr))
    elif chain_upper == "BTC":
        return bool(BTC_ADDRESS_REGEX.match(clean_addr))

    return False


def safe_parse_amount(raw_amount: str, decimals: int = 18) -> Optional[Decimal]:
    """Safely parse human-readable token amounts into Decimal with edge-case handling."""
    if not isinstance(raw_amount, (str, int, float)) or isinstance(raw_amount, bool):
        return None

    if isinstance(decimals, bool) or not isinstance(decimals, int) or decimals < 0 or decimals > 36:
        return None

    try:
        val_str = str(raw_amount).strip()
        if not val_str or val_str.lower() in ("nan", "inf", "-inf", "infinity", "-infinity"):
            return None

        amount = Decimal(val_str)

        # Prevent negative, infinite, or NaN values
        if amount < 0 or amount.is_infinite() or amount.is_nan():
            return None

        # Verify precision does not exceed specified decimal ceiling
        exponent = abs(amount.as_tuple().exponent)
        if isinstance(exponent, int) and exponent > decimals:
            return None

        return amount
    except (InvalidOperation, DecimalException, TypeError, ValueError):
        return None


def validate_tx_hash(tx_hash: str) -> bool:
    """Check if transaction hash complies with standard 32-byte hex format."""
    if not isinstance(tx_hash, str):
        return False

    clean_hash = tx_hash.strip()
    if not clean_hash.startswith("0x") and len(clean_hash) == 64:
        clean_hash = "0x" + clean_hash

    return bool(HEX_32BYTES_REGEX.match(clean_hash))
