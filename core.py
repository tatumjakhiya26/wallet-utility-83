from typing import Dict, List, Optional

class WalletManager:
    def __init__(self, currency_code: str = "BTC"):
        """Initialize the manager with a specific asset."""
        self.currency_code: str = currency_code
        self.balances: Dict[str, float] = {}

    def update_balance(self, address: str, amount: float) -> None:
        """Update the balance for a specific crypto address."""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.balances[address] = amount

    def get_total_assets(self) -> float:
        """Calculate sum of all stored wallet balances."""
        return float(sum(self.balances.values()))

    def list_active_addresses(self) -> List[str]:
        """Return list of addresses with non-zero balance."""
        return [addr for addr, bal in self.balances.items() if bal > 0]

    def fetch_transaction_history(self, address: str) -> Optional[List[str]]:
        """Simulate retrieval of ledger data for address."""
        if address not in self.balances:
            return None
        return [f"tx_hash_{address[:4]}"]