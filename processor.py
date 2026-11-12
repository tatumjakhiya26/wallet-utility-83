import logging

class TransactionError(Exception):
    pass

def process_transaction(wallet_data: dict, amount: float) -> bool:
    """Validates and processes wallet transactions with edge case handling."""
    logger = logging.getLogger(__name__)
    
    try:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise TransactionError(f"Invalid transaction amount: {amount}")
        
        balance = wallet_data.get("balance", 0)
        if balance < amount:
            raise TransactionError("Insufficient funds in wallet")
            
        if "address" not in wallet_data or not wallet_data["address"]:
            raise TransactionError("Missing destination address")
            
        # Simulation of core processing logic
        wallet_data["balance"] -= amount
        return True
        
    except (TypeError, KeyError) as e:
        logger.error(f"Data structure mismatch: {e}")
        return False
    except TransactionError as e:
        logger.warning(f"Transaction rejection: {e}")
        return False
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}")
        return False