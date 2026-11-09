import re
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, List, Tuple

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
BTC_ADDRESS_PATTERN = re.compile(r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,62}$")
SUPPORTED_TYPES = {"transfer", "mint", "burn"}


def validate_transaction_payload(tx: Dict[str, Any]) -> Tuple[bool, str]:
    """Validates individual transaction fields before processing."""
    if not isinstance(tx, dict):
        return False, "Transaction item must be a dictionary"

    address = tx.get("address")
    if not address or not isinstance(address, str):
        return False, "Missing or non-string wallet address"

    if not (ETH_ADDRESS_PATTERN.match(address) or BTC_ADDRESS_PATTERN.match(address)):
        return False, "Invalid cryptocurrency address format"

    raw_amount = tx.get("amount")
    if raw_amount is None:
        return False, "Missing transaction amount"

    try:
        amount = Decimal(str(raw_amount))
        if amount <= 0:
            return False, "Amount must be strictly positive"
    except (InvalidOperation, TypeError, ValueError):
        return False, "Amount is not a valid numeric value"

    tx_type = str(tx.get("type", "")).lower()
    if tx_type not in SUPPORTED_TYPES:
        return False, f"Unsupported transaction type: '{tx_type}'"

    return True, "Valid"


def process_transaction_batch(queue: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Main processing loop with input validation for queued transactions."""
    processed = []
    rejected = []

    for idx, tx_item in enumerate(queue):
        is_valid, reason = validate_transaction_payload(tx_item)
        if not is_valid:
            rejected.append({"index": idx, "payload": tx_item, "reason": reason})
            continue

        processed.append({
            "index": idx,
            "address": tx_item["address"],
            "amount": str(Decimal(str(tx_item["amount"]))),
            "type": str(tx_item["type"]).lower(),
            "status": "validated"
        })

    return {
        "total_count": len(queue),
        "processed_count": len(processed),
        "rejected_count": len(rejected),
        "processed": processed,
        "rejected": rejected
    }
