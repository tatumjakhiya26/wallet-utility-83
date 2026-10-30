import logging
from typing import Optional, Union

logger = logging.getLogger(__name__)

def validate_address(address: str) -> bool:
    """Verify basic crypto address structure."""
    if not isinstance(address, str) or len(address) < 26 or len(address) > 42:
        return False
    return address.isalnum()

def parse_amount(value: Union[str, float, int]) -> Optional[float]:
    """Sanitize input amount for transactions."""
    try:
        amount = float(value)
        if amount < 0:
            logger.error(f"Negative amount provided: {amount}")
            return None
        return amount
    except (ValueError, TypeError) as e:
        logger.warning(f"Invalid amount format: {value} - {e}")
        return None

def format_gas_fee(fee: float) -> str:
    """Ensure gas fee is positive and correctly formatted."""
    if fee <= 0:
        logger.info("Using default zero gas fee")
        return "0.0"
    return f"{fee:.8f}"

def safe_execute(func, *args, **kwargs):
    """Wrap core operations in error boundary."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.error(f"Critical execution failure: {e}", exc_info=True)
        return None