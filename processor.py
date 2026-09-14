import decimal
from typing import Dict, Optional

# wallet-utility-83: utility for crypto data handling

def normalize_amount(amount: str, decimals: int = 18) -> decimal.Decimal:
    """Converts raw chain integer strings to decimal format."""
    try:
        factor = decimal.Decimal(10) ** decimals
        return decimal.Decimal(amount) / factor
    except (decimal.InvalidOperation, ValueError):
        return decimal.Decimal('0')

def format_crypto_value(value: decimal.Decimal, precision: int = 8) -> str:
    """Formats decimal values for UI display."""
    quantizer = decimal.Decimal('1.' + '0' * precision)
    return str(value.quantize(quantizer, rounding=decimal.ROUND_HALF_UP))

def extract_tx_metadata(raw_data: Dict) -> Dict[str, Optional[str]]:
    """Parses core transaction fields from provider response."""
    return {
        'hash': raw_data.get('hash') or raw_data.get('tx_hash'),
        'sender': raw_data.get('from', '').lower(),
        'recipient': raw_data.get('to', '').lower(),
        'status': 'confirmed' if raw_data.get('status') == 1 else 'pending'
    }

if __name__ == '__main__':
    # Example usage for wallet-utility-83 context
    raw_val = '1500000000000000000'
    clean_val = normalize_amount(raw_val)
    print(f"Normalized: {format_crypto_value(clean_val)}")