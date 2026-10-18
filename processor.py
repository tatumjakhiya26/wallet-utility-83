import re

# crypto address validation patterns
ADDRESS_PATTERN = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')

def validate_input(data: dict) -> bool:
    """Ensures wallet operations receive valid data types and formats."""
    address = data.get('address', '')
    amount = data.get('amount', 0)

    if not isinstance(address, str) or not ADDRESS_PATTERN.match(address):
        return False
    
    if not isinstance(amount, (int, float)) or amount <= 0:
        return False

    return True

def process_wallet_queue(queue: list):
    """Main processing loop for wallet transaction tasks."""
    for task in queue:
        try:
            if not validate_input(task):
                print(f"Skipping invalid task: {task}")
                continue
            
            # proceed with signing and broadcast logic
            print(f"Processing transaction to {task['address']} for {task['amount']} BTC")
            
        except Exception as e:
            print(f"Critical failure processing task: {e}")

if __name__ == '__main__':
    sample_tasks = [
        {'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 'amount': 0.05},
        {'address': 'invalid-address', 'amount': 1.0}
    ]
    process_wallet_queue(sample_tasks)