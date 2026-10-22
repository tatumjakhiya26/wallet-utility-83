import re
from typing import Dict, List, Any, Optional

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


def validate_transaction_input(data: Dict[str, Any]) -> Optional[str]:
    """Validate single transaction payload fields."""
    address = data.get("address")
    if not address or not isinstance(address, str):
        return "missing or invalid address field"

    if not ETH_ADDRESS_PATTERN.match(address):
        return f"invalid ethereum address format: {address}"

    amount = data.get("amount")
    if amount is None or not isinstance(amount, (int, float)):
        return "amount must be a numeric value"

    if amount <= 0:
        return f"amount must be greater than zero, got {amount}"

    return None


def process_transaction_queue(batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Main processing loop with input validation for transaction batches."""
    results = []

    for index, item in enumerate(batch):
        error = validate_transaction_input(item)
        if error:
            results.append({
                "index": index,
                "status": "rejected",
                "reason": error
            })
            continue

        results.append({
            "index": index,
            "status": "processed",
            "address": item["address"].lower(),
            "amount": float(item["amount"])
        })

    return results
