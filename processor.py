import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class TransactionProcessor:
    """Handles crypto transaction validation and batch processing."""

    def __init__(self, network: str = "mainnet"):
        self.network = network

    def validate_tx(self, tx: Dict[str, Any]) -> bool:
        """Basic integrity check for raw transaction data."""
        required_fields = {"sender", "receiver", "amount", "nonce"}
        return all(field in tx for field in required_fields)

    def process_batch(self, transactions: List[Dict[str, Any]]) -> Dict[str, int]:
        """Filters and counts successful transactions from a list."""
        results = {"success": 0, "failed": 0}
        
        for tx in transactions:
            try:
                if self.validate_tx(tx):
                    results["success"] += 1
                else:
                    results["failed"] += 1
            except Exception as e:
                logger.error(f"Unexpected processing error: {e}")
                results["failed"] += 1
        
        return results

    def format_status(self, results: Dict[str, int]) -> str:
        """Provides a summary string for UI or logging output."""
        return f"Processed {sum(results.values())} txs: {results['success']} OK, {results['failed']} ERR"