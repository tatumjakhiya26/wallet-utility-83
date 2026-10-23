import decimal
from typing import Dict, Optional

# Configuration for precision handling in wallet operations
SATOSHI_UNIT = decimal.Decimal('100000000')

def normalize_amount(amount: str) -> decimal.Decimal:
    """Converts raw string amount to decimal with standard crypto precision."""
    try:
        return decimal.Decimal(amount).quantize(decimal.Decimal('0.00000001'), rounding=decimal.ROUND_HALF_UP)
    except decimal.InvalidOperation:
        return decimal.Decimal('0.00000000')

def calculate_fee(amount_sats: int, fee_rate: float) -> int:
    """Calculates network transaction fee based on current rate."""
    return int(amount_sats * fee_rate)

def format_wallet_balance(balance_data: Dict[str, str]) -> Dict[str, float]:
    """Converts dictionary of raw amounts to float representation for UI."""
    processed = {}
    for currency, value in balance_data.items():
        decimal_val = normalize_amount(value)
        processed[currency] = float(decimal_val)
    return processed

if __name__ == '__main__':
    # Example usage for wallet-utility-83 core logic
    raw_balances = {"BTC": "0.00543210", "ETH": "1.23456789"}
    print(format_wallet_balance(raw_balances))