import hashlib
import json
from typing import Dict, Any


class CryptoDataHandler:
    """Utility class for parsing and formatting cryptocurrency transaction payloads."""

    DECIMAL_FACTORS = {
        "BTC": 10**8,
        "ETH": 10**18,
        "SOL": 10**9,
    }

    @staticmethod
    def convert_to_base_unit(amount: float, symbol: str) -> int:
        """Convert standard unit amount to smallest denomination."""
        symbol_upper = symbol.upper()
        if symbol_upper not in CryptoDataHandler.DECIMAL_FACTORS:
            raise ValueError(f"Unsupported crypto symbol: {symbol}")
        return int(amount * CryptoDataHandler.DECIMAL_FACTORS[symbol_upper])

    @staticmethod
    def generate_tx_hash(payload: Dict[str, Any]) -> str:
        """Generate a deterministic SHA-256 hash for a given payload."""
        serialized = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(serialized).hexdigest()

    @classmethod
    def process_raw_transaction(cls, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize and process raw incoming crypto transaction payload."""
        required_fields = ["sender", "recipient", "amount", "asset"]
        for field in required_fields:
            if field not in raw_data:
                raise KeyError(f"Missing required payload field: {field}")

        symbol = raw_data["asset"].upper()
        amount_base = cls.convert_to_base_unit(float(raw_data["amount"]), symbol)

        processed_payload = {
            "sender": str(raw_data["sender"]).strip(),
            "recipient": str(raw_data["recipient"]).strip(),
            "amount_base": amount_base,
            "asset": symbol,
            "memo": raw_data.get("memo", ""),
            "timestamp": raw_data.get("timestamp"),
        }

        processed_payload["tx_hash"] = cls.generate_tx_hash(processed_payload)
        return processed_payload
