import json
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, Optional

class CryptoDataHandler:
    """Utility class for wallet balance and unit calculations."""

    PRECISION = 8

    @staticmethod
    def format_amount(amount: float) -> str:
        """Convert float amount to string with 8-decimal precision."""
        val = Decimal(str(amount))
        return f"{val.quantize(Decimal('1.' + '0' * CryptoDataHandler.PRECISION), rounding=ROUND_HALF_UP)}"

    @staticmethod
    def validate_tx_payload(data: Dict[str, Any]) -> bool:
        """Verify basic transaction payload structure."""
        required_fields = {'sender', 'receiver', 'amount', 'currency'}
        return all(field in data for field in required_fields)

    @classmethod
    def sanitize_balance(cls, balance_data: Dict[str, Any]) -> Dict[str, str]:
        """Normalize balance fields for API responses."""
        return {
            "address": str(balance_data.get("address", "")),
            "balance": cls.format_amount(balance_data.get("amount", 0.0)),
            "currency": str(balance_data.get("currency", "BTC").upper())
        }

def process_wallet_data(raw_input: str) -> Optional[Dict[str, str]]:
    """Entry point for incoming crypto stream processing."""
    try:
        data = json.loads(raw_input)
        if CryptoDataHandler.validate_tx_payload(data):
            return CryptoDataHandler.sanitize_balance(data)
    except (json.JSONDecodeError, ValueError):
        return None
    return None