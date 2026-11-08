import logging
from decimal import Decimal, InvalidOperation
from typing import Optional

logger = logging.getLogger(__name__)

class WalletError(Exception):
    """Base exception for wallet operations."""
    pass

def validate_transaction(amount: str, balance: str) -> bool:
    """Validates transaction amount against available balance."""
    try:
        dec_amount = Decimal(amount)
        dec_balance = Decimal(balance)
        
        if dec_amount <= 0:
            logger.warning("transaction failed: non-positive amount")
            return False
        
        if dec_amount > dec_balance:
            logger.warning("transaction failed: insufficient funds")
            return False
            
        return True
    except (InvalidOperation, ValueError, TypeError) as e:
        logger.error(f"validation error: invalid input format - {e}")
        return False

def process_withdrawal(amount: str, balance: str) -> Optional[Decimal]:
    """Safely processes a withdrawal request with edge case handling.""
    if not validate_transaction(amount, balance):
        return None
        
    try:
        new_balance = Decimal(balance) - Decimal(amount)
        return new_balance
    except Exception as e:
        logger.critical(f"unexpected calculation error: {e}")
        raise WalletError("critical wallet transaction failure") from e