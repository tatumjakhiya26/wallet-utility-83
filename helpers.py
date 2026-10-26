"""
Crypto data conversion and balance formatting utilities.
"""

from decimal import Decimal, ROUND_DOWN
from typing import Union, Dict

# Standard precision map for popular cryptocurrencies (decimals)
TOKEN_DECIMALS: Dict[str, int] = {
    "BTC": 8,
    "ETH": 18,
    "USDT": 6,
    "USDC": 6,
    "SOL": 9,
    "BNB": 18,
    "DOGE": 8,
}


def raw_to_decimal(amount: Union[int, str], symbol: str) -> Decimal:
    """Convert raw smallest currency units (e.g., Satoshis, Wei) to Decimal."""
    decimals = TOKEN_DECIMALS.get(symbol.upper(), 18)
    factor = Decimal(10) ** decimals
    return Decimal(str(amount)) / factor


def decimal_to_raw(amount: Union[float, str, Decimal], symbol: str) -> int:
    """Convert base token units to smallest raw integer units."""
    decimals = TOKEN_DECIMALS.get(symbol.upper(), 18)
    factor = Decimal(10) ** decimals
    converted = Decimal(str(amount)) * factor
    return int(converted.quantize(Decimal("1"), rounding=ROUND_DOWN))


def format_crypto_balance(
    amount: Union[Decimal, float, str], precision: int = 4, symbol: str = ""
) -> str:
    """Format numeric balance with optional token symbol and fixed precision."""
    dec_val = Decimal(str(amount))
    quantizer = Decimal("10") ** -precision
    formatted_val = dec_val.quantize(quantizer, rounding=ROUND_DOWN)

    val_str = f"{formatted_val:f}"
    if symbol:
        return f"{val_str} {symbol.upper()}"
    return val_str
