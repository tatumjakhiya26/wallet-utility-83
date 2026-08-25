import re
import hashlib
from typing import Dict, Any

class WalletProcessor:
    """Processor for crypto wallet operations."""

    def __init__(self) -> None:
        self.wallets: Dict[str, Dict[str, Any]] = {}

    def process_wallet(self, address: str, private_key: str) -> float:
        """Process a wallet address and return simulated balance."""
        if not self._is_valid_address(address):
            raise ValueError("Invalid wallet address format")
        balance = self._compute_balance(address)
        self.wallets[address] = {
            "balance": balance,
            "key_hint": private_key[:6] + "****"
        }
        return balance

    def _is_valid_address(self, address: str) -> bool:
        """Validate address using simple pattern for demo purposes."""
        # Supports common formats like BTC and ETH
        btc_pattern = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
        eth_pattern = r"^0x[a-fA-F0-9]{40}$"
        return bool(re.match(btc_pattern, address) or re.match(eth_pattern, address))

    def _compute_balance(self, address: str) -> float:
        """Simulate balance calculation using hash."""
        hash_val = int(hashlib.sha256(address.encode()).hexdigest(), 16)
        return round((hash_val % 10000) / 100, 2)

    def cleanup_wallets(self) -> int:
        """Remove any invalid entries from storage."""
        invalid = [addr for addr in list(self.wallets.keys()) if not self._is_valid_address(addr)]
        for addr in invalid:
            del self.wallets[addr]
        return len(invalid)

    def get_wallet_summary(self) -> Dict[str, Any]:
        """Return summary of processed wallets."""
        if not self.wallets:
            return {"count": 0, "total_balance": 0.0}
        total = sum(w["balance"] for w in self.wallets.values())
        return {
            "count": len(self.wallets),
            "total_balance": total,
            "average_balance": round(total / len(self.wallets), 2)
        }

# Demonstration of usage
if __name__ == "__main__":
    processor = WalletProcessor()
    processor.process_wallet("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "demo_private_key_123")
    processor.process_wallet("0x742d35Cc6634C0532925a3b844Bc454e4438f44e", "demo_key_456")
    summary = processor.get_wallet_summary()
    print(summary)
    cleaned = processor.cleanup_wallets()
    print(f"Cleaned {cleaned} wallets")