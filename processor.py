from typing import Dict, List, Optional
from decimal import Decimal

def calculate_balance(transactions: List[Dict[str, str]]) -> Decimal:
    """
    Aggregates net balance from a list of transaction objects.
    Each dict expects 'type' (credit/debit) and 'amount' keys.
    """
    balance = Decimal('0.0')
    for tx in transactions:
        amount = Decimal(tx.get('amount', '0.0'))
        if tx.get('type') == 'credit':
            balance += amount
        elif tx.get('type') == 'debit':
            balance -= amount
    return balance

def format_crypto_address(address: str, prefix_len: int = 6) -> str:
    """
    Truncates long crypto addresses for display purposes.
    """
    if len(address) <= (prefix_len * 2) + 3:
        return address
    return f"{address[:prefix_len]}...{address[-prefix_len:]}"

def validate_transaction_fee(fee: Decimal, min_fee: Decimal) -> bool:
    """
    Verifies that the transaction fee meets network minimums.
    """
    return fee >= min_fee