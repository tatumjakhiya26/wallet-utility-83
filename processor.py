import logging
import re

# Configure logging for wallet transactions
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_valid_address(address: str) -> bool:
    """Validate cryptocurrency wallet address format."""
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def process_transaction(data: dict):
    """Process validated transaction data."""
    addr = data.get('address', '')
    amount = data.get('amount', 0)

    if not is_valid_address(addr):
        logger.warning(f"Invalid address format: {addr}")
        return False
    
    if not isinstance(amount, (int, float)) or amount <= 0:
        logger.warning(f"Invalid transaction amount: {amount}")
        return False

    logger.info(f"Processing {amount} units to {addr}")
    return True

def run_main_loop(queue):
    """Main processing loop for wallet operations."""
    while True:
        try:
            tx = queue.get()
            if not tx:
                break
            
            if process_transaction(tx):
                logger.info("Transaction successfully dispatched")
            else:
                logger.error("Transaction validation failed")
        except Exception as e:
            logger.error(f"Critical processing error: {e}")