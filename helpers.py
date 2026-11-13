import decimal
from typing import Union

def normalize_amount(amount: Union[str, float, int]) -> decimal.Decimal:
    """Converts varying input types to precise Decimal for crypto math."""
    return decimal.Decimal(str(amount)).quantize(decimal.Decimal('0.00000001'), rounding=decimal.ROUND_DOWN)

def format_address(address: str) -> str:
    """Standardizes address string format for blockchain compatibility."""
    return address.strip().lower()

def validate_fee_rate(fee: float) -> bool:
    """Ensures fee remains within sane protocol bounds."""
    return 0.00000001 <= fee <= 0.1

def format_transaction_summary(tx_id: str, amount: decimal.Decimal) -> str:
    """Consistent reporting format for wallet logs."""
    return f"TX[{tx_id}]: {amount.normalize()} units processed"