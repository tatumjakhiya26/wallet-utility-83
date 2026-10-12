import logging
from typing import Optional, Dict

# Configure structured logging for wallet operations
logger = logging.getLogger('wallet-utility-83')

def format_address(address: str) -> str:
    """Standardize hex addresses to checksum format."""
    if not address.startswith('0x'):
        return f'0x{address.lower()}'
    return address.lower()

def validate_balance_format(balance: float) -> bool:
    """Ensure balance is non-negative and finite."""
    return isinstance(balance, (int, float)) and balance >= 0

def safe_log_transaction(tx_data: Dict) -> None:
    """Secure logging for sensitive transaction metadata."""
    tx_id = tx_data.get('hash', 'unknown')
    status = tx_data.get('status', 'pending')
    logger.info(f'Transaction {tx_id} status updated to {status}')

def get_environment_config(key: str, default: Optional[str] = None) -> str:
    """Safe retrieval of environment variables."""
    import os
    return os.getenv(key, default) or ''

# Utility constants for transaction limits
MIN_GAS_LIMIT = 21000
MAX_TX_RETRY_ATTEMPTS = 3