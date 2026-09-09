import re
from typing import Dict, Any, List

# Regex patterns for validation
EVM_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")

def validate_evm_address(address: str) -> bool:
    """Check if the address matches standard EVM 40-character hex pattern."""
    if not isinstance(address, str):
        return False
    return bool(EVM_ADDRESS_PATTERN.match(address))

def validate_amount(amount: Any) -> bool:
    """Ensure the transaction amount is a positive number."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def process_transaction_queue(transactions: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    """
    Main processing loop validating and filtering incoming transaction requests.
    Returns categorized lists of successful and failed transaction processing.
    """
    processed_txs = []
    failed_txs = []

    for idx, tx in enumerate(transactions):
        if not isinstance(tx, dict):
            failed_txs.append({"index": idx, "error": "Invalid transaction format, expected dict"})
            continue

        to_address = tx.get("to_address")
        amount = tx.get("amount")
        tx_id = tx.get("tx_id", f"unknown_{idx}")

        # Validate receiver address
        if not validate_evm_address(to_address):
            failed_txs.append({"tx_id": tx_id, "error": f"Invalid destination address: {to_address}"})
            continue

        # Validate amount value
        if not validate_amount(amount):
            failed_txs.append({"tx_id": tx_id, "error": f"Invalid amount: {amount}"})
            continue

        # If validations pass, proceed to log successful preparation
        processed_txs.append({
            "tx_id": tx_id,
            "to_address": to_address,
            "amount": float(amount),
            "status": "validated_and_ready"
        })

    return {"processed": processed_txs, "failed": failed_txs}