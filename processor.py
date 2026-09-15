import re
from typing import Dict, List, Any


class TransactionProcessor:
    """Processes incoming crypto transactions with strict input validation."""

    ETH_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
    SUPPORTED_CURRENCIES = {"BTC", "ETH", "USDT", "SOL"}

    def __init__(self, raw_queue: List[Dict[str, Any]]):
        self.raw_queue = raw_queue
        self.processed_items: List[Dict[str, Any]] = []
        self.failed_items: List[Dict[str, Any]] = []

    def validate_item(self, item: Dict[str, Any]) -> bool:
        """Validates raw transaction dictionary structure and values."""
        if not isinstance(item, dict):
            return False

        address = item.get("address")
        amount = item.get("amount")
        currency = item.get("currency")

        if not address or not isinstance(address, str):
            return False
        if not self.ETH_ADDRESS_REGEX.match(address):
            return False

        if not isinstance(amount, (int, float)) or amount <= 0:
            return False

        if not currency or currency.upper() not in self.SUPPORTED_CURRENCIES:
            return False

        return True

    def run() -> Dict[str, int]:
        """Main processing loop that validates and dispatches transactions."""
        for item in self.raw_queue:
            if not self.validate_item(item):
                self.failed_items.append({"item": item, "reason": "invalid_payload"})
                continue

            sanitized_item = {
                "address": item["address"].lower(),
                "amount": float(item["amount"]),
                "currency": item["currency"].upper(),
                "status": "validated"
            }
            self.processed_items.append(sanitized_item)

        return {
            "processed": len(self.processed_items),
            "failed": len(self.failed_items)
        }
