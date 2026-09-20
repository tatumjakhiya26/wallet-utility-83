import logging
import re

# regex for crypto address validation
ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

def validate_input(data: dict) -> bool:
    """Ensures wallet operations receive valid inputs."""
    if 'address' not in data or not ADDRESS_PATTERN.match(data['address']):
        logging.error("Invalid wallet address format")
        return False
    if not isinstance(data.get('amount'), (int, float)) or data['amount'] <= 0:
        logging.error("Invalid transaction amount")
        return False
    return True

def process_transactions(queue: list):
    """Main processing loop for wallet operations."""
    for entry in queue:
        try:
            if not validate_input(entry):
                continue
            
            # proceed with wallet logic
            logging.info(f"Processing transaction for {entry['address']}")
        except KeyError as e:
            logging.error(f"Malformed transaction object: {e}")
        except Exception as e:
            logging.critical(f"Unexpected error during processing: {e}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sample_queue = [{'address': '0x1234567890abcdef1234567890abcdef12345678', 'amount': 1.5}]
    process_transactions(sample_queue)