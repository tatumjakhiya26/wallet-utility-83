import json
import hashlib
from typing import Dict, Any, Optional

class TransactionHandler:
    """Handles processing, signing, and verification of crypto wallet transactions."""

    def __init__(self, wallet_address: str, private_key: str) -> None:
        """Initialize the transaction handler with wallet credentials."""
        self.wallet_address = wallet_address
        self._private_key = private_key

    def create_transaction(self, recipient: str, amount: float, fee: float) -> Dict[str, Any]:
        """Create and format a standard transaction payload.

        Args:
            recipient: The target wallet address.
            amount: The amount of cryptocurrency to transfer.
            fee: The transaction gas/network fee.

        Returns:
            A dictionary containing the unsigned transaction payload.
        """
        return {
            "sender": self.wallet_address,
            "recipient": recipient,
            "amount": amount,
            "fee": fee,
            "nonce": 1
        }

    def sign_transaction(self, tx_payload: Dict[str, Any]) -> str:
        """Generate a mock cryptographic signature for the transaction.

        Args:
            tx_payload: The transaction payload to be signed.

        Returns:
            A hex string representing the transaction signature.
        """
        serialized_tx = json.dumps(tx_payload, sort_keys=True)
        raw_signature = f"{serialized_tx}{self._private_key}"
        return hashlib.sha256(raw_signature.encode('utf-8')).hexdigest()

    def process_payment(self, recipient: str, amount: float, fee: float) -> Optional[Dict[str, Any]]:
        """Execute transaction generation and signing sequence.

        Args:
            recipient: The destination wallet address.
            amount: Transfer amount in cryptocurrency.
            fee: Network transaction fee.

        Returns:
            The fully signed transaction payload, or None if validation fails.
        """
        if not recipient or amount <= 0 or fee < 0:
            return None

        tx = self.create_transaction(recipient, amount, fee)
        signature = self.sign_transaction(tx)
        tx["signature"] = signature
        return tx