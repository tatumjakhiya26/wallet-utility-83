from typing import List, Dict, Optional, Union

class TransactionProcessor:
    """Handles crypto transaction validation and normalization."""

    def __init__(self, network: str = "mainnet") -> None:
        self.network = network

    def validate_address(self, address: str) -> bool:
        """Verify basic crypto address format integrity."""
        return len(address) > 25 and address.isalnum()

    def process_batch(self, transactions: List[Dict[str, Union[str, float]]]) -> List[Dict[str, Optional[bool]]]:
        """Validates a list of transactions against network rules."""
        results = []
        for tx in transactions:
            address = str(tx.get("address", ""))
            amount = float(tx.get("amount", 0))
            
            is_valid = self.validate_address(address) and amount > 0
            results.append({
                "tx_id": tx.get("id"),
                "status": "success" if is_valid else "failed"
            })
        return results

    def get_summary(self, processed: List[Dict]) -> Dict[str, int]:
        """Aggregate report of processing results."""
        total = len(processed)
        successes = sum(1 for item in processed if item["status"] == "success")
        return {"total": total, "success": successes, "failure": total - successes}