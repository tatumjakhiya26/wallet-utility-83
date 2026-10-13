import logging

logger = logging.getLogger(__name__)

class TransactionError(Exception):
    """Base exception for transaction processing"""
    pass

def process_transaction(wallet_address: str, amount: float) -> dict:
    """Validates and processes crypto transaction with robust error handling"""
    try:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid transaction amount: must be positive numeric")
        
        if len(wallet_address) != 42 or not wallet_address.startswith('0x'):
            raise ValueError("Invalid wallet address format")

        # Simulated processing logic
        status = {"status": "success", "address": wallet_address, "amount": amount}
        logger.info(f"Processed {amount} for {wallet_address}")
        return status

    except ValueError as ve:
        logger.error(f"Validation failure: {ve}")
        return {"status": "failed", "error": str(ve)}
    except Exception as e:
        logger.critical(f"Unexpected system error: {e}")
        return {"status": "error", "error": "internal system failure"}

def batch_process(transactions: list) -> list:
    """Handles batch processing with individual item error isolation"""
    results = []
    for tx in transactions:
        res = process_transaction(tx.get('addr', ''), tx.get('amt', 0))
        results.append(res)
    return results