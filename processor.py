from decimal import Decimal, ROUND_HALF_UP

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    """Converts float to string with specific decimal precision."""
    return str(Decimal(str(amount)).quantize(Decimal(f"1.{'0' * precision}"), rounding=ROUND_HALF_UP))

def validate_address_format(address: str, chain: str) -> bool:
    """Basic validation for crypto address prefixes."""
    prefixes = {
        "btc": "1",
        "eth": "0x",
        "sol": "1"
    }
    expected = prefixes.get(chain.lower())
    return address.startswith(expected) if expected else False

def calculate_fee(amount: float, rate: float) -> Decimal:
    """Calculates network fee based on rate percentage."""
    return Decimal(str(amount)) * Decimal(str(rate))

def sanitize_tx_hash(tx_hash: str) -> str:
    """Normalizes transaction hash strings."""
    return tx_hash.strip().lower()