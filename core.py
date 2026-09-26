from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class WalletData:
    address: str
    balance: float
    currency: str

def validate_address(address: str) -> bool:
    """Verify basic crypto address structure."""
    return len(address) >= 26 and len(address) <= 42

class WalletManager:
    def __init__(self) -> None:
        self.wallets: Dict[str, WalletData] = {}

    def add_wallet(self, address: str, balance: float, currency: str = "BTC") -> None:
        """Register a new wallet to the internal tracking system."""
        if validate_address(address):
            self.wallets[address] = WalletData(address, balance, currency)

    def get_total_balance(self, currency: str) -> float:
        """Calculate aggregate balance for a specific currency."""
        total: float = 0.0
        for wallet in self.wallets.values():
            if wallet.currency == currency:
                total += wallet.balance
        return total

    def list_addresses(self) -> List[str]:
        """Return list of all tracked wallet addresses."""
        return list(self.wallets.keys())