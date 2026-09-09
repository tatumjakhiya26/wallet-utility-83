import logging
from typing import Dict

class CryptoError(Exception):
    """Base exception for crypto wallet utilities."""
    pass

class InsufficientFundsError(CryptoError):
    """Raised when the wallet balance is less than the transaction amount."""
    pass

class InvalidAddressError(CryptoError):
    """Raised when a public key or wallet address fails validation."""
    pass

class TransactionProcessor:
    """Handles secure transfer validation and balance updates for simulated assets."""
    
    def __init__(self, initial_balances: Dict[str, float]):
        self.balances = initial_balances
        self.logger = logging.getLogger("processor")

    def validate_address(self, address: str) -> None:
        """Validates standard hex address format."""
        if not isinstance(address, str) or not address.startswith("0x") or len(address) != 42:
            raise InvalidAddressError(f"Address '{address}' is not a valid hex address.")

    def transfer(self, sender: str, recipient: str, amount: float) -> str:
        """Executes a secure transfer between two addresses with strict error handling."""
        self.validate_address(sender)
        self.validate_address(recipient)

        if amount <= 0:
            raise ValueError("Transaction amount must be strictly greater than zero.")

        sender_balance = self.balances.get(sender, 0.0)
        if sender_balance < amount:
            raise InsufficientFundsError(
                f"Insufficient funds at {sender}. Available: {sender_balance}, Requested: {amount}"
            )

        # Execution phase with double-entry safety
        self.balances[sender] -= amount
        self.balances[recipient] = self.balances.get(recipient, 0.0) + amount

        self.logger.info(f"Successfully transferred {amount} from {sender} to {recipient}")
        return f"tx_hash_{hash((sender, recipient, amount))}"