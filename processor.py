import logging

class TransactionError(Exception):
    """Base exception for transaction processing issues."""
    pass

def process_transaction(tx_data: dict) -> bool:
    """Validates and processes cryptocurrency transaction data."""
    required_fields = ['amount', 'sender', 'receiver']
    
    try:
        # Check for missing data
        if not all(k in tx_data for k in required_fields):
            raise TransactionError(f"Missing fields: {required_fields}")
        
        # Check for non-positive amounts
        if tx_data['amount'] <= 0:
            raise ValueError("Transaction amount must be positive")
            
        # Simulation of chain interaction
        logging.info(f"Processing {tx_data['amount']} from {tx_data['sender']}")
        return True
        
    except ValueError as ve:
        logging.error(f"Data validation failure: {ve}")
        return False
    except KeyError as ke:
        logging.error(f"Schema inconsistency: {ke}")
        return False
    except Exception as e:
        logging.critical(f"Unexpected system failure: {e}")
        raise TransactionError("Internal processing error") from e