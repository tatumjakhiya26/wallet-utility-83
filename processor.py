import re
from typing import Dict, Any, List, Tuple


def is_valid_eth_address(address: str) -> bool:
    """Check if the provided string is a valid Ethereum address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def validate_transaction_payload(payload: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate incoming transaction payload structure and values."""
    required_fields = ["sender", "recipient", "amount", "chain_id"]
    for field in required_fields:
        if field not in payload:
            return False, f"Missing required field: {field}"

    if not is_valid_eth_address(payload["sender"]):
        return False, "Invalid sender wallet address format"

    if not is_valid_eth_address(payload["recipient"]):
        return False, "Invalid recipient wallet address format"

    amount = payload.get("amount")
    if not isinstance(amount, (int, float)) or amount <= 0:
        return False, f"Invalid transaction amount: {amount}"

    chain_id = payload.get("chain_id")
    if not isinstance(chain_id, int) or chain_id <= 0:
        return False, f"Invalid network chain_id: {chain_id}"

    return True, "Valid payload"


def process_transaction_queue(queue: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Main processing loop that validates and segregates transaction payloads."""
    processed = []
    rejected = []

    for idx, item in enumerate(queue):
        is_valid, reason = validate_transaction_payload(item)
        if not is_valid:
            rejected.append({"index": idx, "payload": item, "reason": reason})
            continue

        processed_item = {
            "tx_id": f"tx_{idx}_{item['chain_id']}",
            "sender": item["sender"].lower(),
            "recipient": item["recipient"].lower(),
            "amount": float(item["amount"]),
            "chain_id": item["chain_id"],
            "status": "ready",
        }
        processed.append(processed_item)

    return {
        "summary": {"total": len(queue), "accepted": len(processed), "rejected": len(rejected)},
        "processed": processed,
        "rejected": rejected,
    }
