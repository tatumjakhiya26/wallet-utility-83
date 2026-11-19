import logging
from decimal import Decimal, InvalidOperation

logger = logging.getLogger(__name__)

def sanitize_amount(amount_str: str) -> Decimal:
    """Converts string input to Decimal with robust error handling."""
    try:
        if not amount_str:
            raise ValueError("Amount string is empty")
        
        amount = Decimal(str(amount_str))
        
        if amount < 0:
            raise ValueError(f"Negative amount provided: {amount}")
            
        return amount
    except (InvalidOperation, ValueError) as e:
        logger.error(f"Invalid crypto amount format: {amount_str} - {str(e)}")
        raise ValueError("Invalid financial amount format")

def validate_address(address: str, expected_prefix: str = "0x") -> bool:
    """Checks basic wallet address structure."""
    if not isinstance(address, str):
        return False
    
    # Check length and prefix for typical EVM-like addresses
    if len(address) != 42 or not address.startswith(expected_prefix):
        logger.warning(f"Malformed address detected: {address}")
        return False
        
    return all(c in "0123456789abcdefABCDEF" for c in address[2:])

def format_crypto_display(amount: Decimal, precision: int = 8) -> str:
    """Formats decimal to string for UI display."""
    try:
        return f"{amount:.{precision}f}".rstrip('0').rstrip('.')
    except (TypeError, ValueError) as e:
        logger.exception("Formatting error in crypto display")
        return "0.00"