import re
from decimal import Decimal, InvalidOperation
from typing import Dict, Any

class WalletError(Exception):
    """Base exception for wallet operations."""
    pass

class InvalidAddressError(WalletError):
    """Raised when a crypto wallet address format is invalid."""
    pass

class InsufficientBalanceError(WalletError):
    """Raised when balance is inadequate for amount plus fee."""
    pass

def validate_and_process_transfer(
    sender: str,
    recipient: str,
    amount_str: str,
    balance_str: str,
    fee_str: str = "0.0005"
) -> Dict[str, Any]:
    """Validates transfer parameters and calculates balances with edge case handling."""
    address_regex = r"^0x[a-fA-F0-9]{40}$"
    
    if not isinstance(sender, str) or not re.match(address_regex, sender):
        raise InvalidAddressError(f"Invalid sender hex address format: {sender}")
        
    if not isinstance(recipient, str) or not re.match(address_regex, recipient):
        raise InvalidAddressError(f"Invalid recipient hex address format: {recipient}")

    if sender.lower() == recipient.lower():
        raise WalletError("Self-transfer to identical address is not allowed.")

    try:
        amount = Decimal(amount_str)
        balance = Decimal(balance_str)
        fee = Decimal(fee_str)
    except (InvalidOperation, TypeError) as err:
        raise WalletError(f"Malformed numerical input: {err}") from err

    if amount <= Decimal("0"):
        raise WalletError(f"Transfer amount must be strictly positive, got: {amount}")

    if fee < Decimal("0"):
        raise WalletError("Transaction fee cannot be negative.")

    total_deduction = amount + fee
    if balance < total_deduction:
        raise InsufficientBalanceError(
            f"Insufficient funds. Required: {total_deduction}, Available: {balance}"
        )

    remaining_balance = balance - total_deduction
    return {
        "status": "success",
        "sender": sender.lower(),
        "recipient": recipient.lower(),
        "amount": str(amount),
        "fee": str(fee),
        "remaining_balance": str(remaining_balance)
    }
