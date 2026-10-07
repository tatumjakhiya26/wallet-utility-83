import logging
from decimal import Decimal, InvalidOperation
from typing import Dict, List, Any

logger = logging.getLogger("wallet_processor")

class TransactionProcessor:
    """
    Utility processor for handling, validating, and aggregating cryptocurrency
    transaction records and denomination conversions.
    """
    def __init__(self, decimals: int = 18):
        self.decimals = decimals

    def to_base_unit(self, amount: str) -> int:
        """
        Convert standard decimal float/string representation to base unit (e.g., Wei).
        """
        try:
            dec_val = Decimal(str(amount))
            return int(dec_val * (Decimal('10') ** self.decimals))
        except (ValueError, InvalidOperation) as err:
            logger.error(f"Conversion failure to base unit for {amount}: {err}")
            raise ValueError(f"Invalid amount format: {amount}")

    def from_base_unit(self, base_amount: int) -> Decimal:
        """
        Convert base unit back to standard decimal representation.
        """
        try:
            return Decimal(base_amount) / (Decimal('10') ** self.decimals)
        except (ValueError, TypeError) as err:
            logger.error(f"Conversion failure from base unit for {base_amount}: {err}")
            raise ValueError(f"Invalid base unit format: {base_amount}")

    def aggregate_wallet_activity(self, address: str, transactions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Filters, validates, and summarizes transaction history for a specific wallet address.
        """
        address_lower = address.lower()
        total_received = Decimal('0')
        total_sent = Decimal('0')
        fees_paid = Decimal('0')
        processed_count = 0

        for tx in transactions:
            # Verify minimum transaction fields
            if not all(k in tx for k in ('from_address', 'to_address', 'value', 'fee')):
                continue

            try:
                tx_from = str(tx['from_address']).lower()
                tx_to = str(tx['to_address']).lower()
                value = Decimal(str(tx['value']))
                fee = Decimal(str(tx['fee']))
            except (ValueError, TypeError, InvalidOperation):
                continue

            if tx_from == address_lower:
                total_sent += value
                fees_paid += fee
                processed_count += 1
            elif tx_to == address_lower:
                total_received += value
                processed_count += 1

        net_balance_change = total_received - (total_sent + fees_paid)

        return {
            "address": address,
            "transactions_processed": processed_count,
            "total_received": str(total_received),
            "total_sent": str(total_sent),
            "fees_paid": str(fees_paid),
            "net_balance_change": str(net_balance_change)
        }
