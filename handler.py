from typing import Dict, Any, Optional

class WalletHandler:
    """Handles crypto wallet operations for specific blockchain networks."""

    def __init__(self, network_id: str, gas_limit: int = 21000) -> None:
        self.network_id = network_id
        self.gas_limit = gas_limit

    def prepare_transaction(self, address: str, amount: float) -> Dict[str, Any]:
        """Formats a transaction payload for signing."""
        return {
            "to": address,
            "value": amount,
            "gas": self.gas_limit,
            "network": self.network_id
        }

    def get_balance_info(self, wallet_id: str) -> Dict[str, float]:
        """Retrieves formatted balance data for a provided wallet address."""
        # Mock balance retrieval
        return {"confirmed": 0.0, "pending": 0.0}

    def validate_request(self, data: Optional[Dict[str, Any]]) -> bool:
        """Ensures incoming request payloads contain required keys."""
        if not data:
            return False
        required_keys = {'to', 'amount'}
        return required_keys.issubset(data.keys())

if __name__ == "__main__":
    handler = WalletHandler(network_id="mainnet")
    payload = handler.prepare_transaction("0xabc", 0.5)
    print(f"Prepared: {payload}")