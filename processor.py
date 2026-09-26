import hashlib
import time
from typing import Dict, Any, List, Optional


class TransactionProcessor:
    """Utility for processing and normalizing raw crypto transaction records."""

    DECIMALS = {
        "BTC": 8,
        "ETH": 18,
        "SOL": 9,
        "USDT": 6,
    }

    def __init__(self, default_symbol: str = "BTC"):
        self.default_symbol = default_symbol.upper()

    def to_base_unit(self, raw_amount: int, symbol: Optional[str] = None) -> float:
        """Convert smallest unit (satoshi/wei) to base currency unit."""
        sym = (symbol or self.default_symbol).upper()
        decimals = self.DECIMALS.get(sym, 8)
        return round(raw_amount / (10 ** decimals), decimals)

    def generate_tx_hash(self, tx_data: Dict[str, Any]) -> str:
        """Generate deterministic internal hash for transaction deduplication."""
        raw_str = f"{tx_data.get('sender')}:{tx_data.get('receiver')}:{tx_data.get('amount')}:{tx_data.get('timestamp')}"
        return hashlib.sha256(raw_str.encode('utf-8')).hexdigest()

    def process_batch(self, raw_txs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process and sanitize a batch of raw wallet transactions."""
        processed = []
        for tx in raw_txs:
            symbol = tx.get("symbol", self.default_symbol).upper()
            raw_amt = int(tx.get("raw_amount", 0))
            
            normalized_tx = {
                "tx_id": tx.get("tx_id") or self.generate_tx_hash(tx),
                "sender": str(tx.get("sender", "")).lower(),
                "receiver": str(tx.get("receiver", "")).lower(),
                "symbol": symbol,
                "amount": self.to_base_unit(raw_amt, symbol),
                "raw_amount": raw_amt,
                "timestamp": tx.get("timestamp", int(time.time())),
                "status": "processed" if raw_amt > 0 else "failed"
            }
            processed.append(normalized_tx)
        return processed