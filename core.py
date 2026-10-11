import logging
from typing import Optional

# Configure logging for wallet operations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('wallet-utility-83')

class WalletError(Exception):
    """Custom exception for wallet operation failures."""
    pass

def validate_address(address: str) -> bool:
    """Check if address length and prefix are valid."""
    if not isinstance(address, str) or len(address) < 26:
        return False
    return address.startswith('0x') or address.startswith('bc1')

def process_transaction(recipient: str, amount: float) -> Optional[str]:
    """
    Execute transaction with validation and error handling.
    Returns transaction hash or None on failure.
    """
    try:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if not validate_address(recipient):
            raise WalletError(f"Invalid address format: {recipient}")

        logger.info(f"Processing {amount} to {recipient}")
        # Simulation of transaction hash generation
        tx_hash = "tx_" + recipient[:8]
        return tx_hash

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return None
    except WalletError as e:
        logger.error(f"Wallet operation error: {e}")
        return None
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}")
        return None