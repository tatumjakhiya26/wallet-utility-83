import re

# Validation patterns for crypto wallet operations
ADDRESS_PATTERN = re.compile(r'^(0x[a-fA-F0-9]{40}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})$')

def validate_input(address: str, amount: float) -> bool:
    """Validates address format and positive transaction amounts."""
    if not ADDRESS_PATTERN.match(address):
        return False
    if not isinstance(amount, (int, float)) or amount <= 0:
        return False
    return True

def process_transactions(queue: list):
    """Main processing loop for wallet transactions with input sanitization."""
    for entry in queue:
        address = entry.get('address')
        amount = entry.get('amount')
        
        if not validate_input(address, amount):
            print(f"Skipping invalid transaction: {address}")
            continue
        
        try:
            execute_transfer(address, amount)
        except Exception as e:
            print(f"Transaction failed for {address}: {e}")

def execute_transfer(address: str, amount: float):
    """Internal handler for blockchain node interaction."""
    print(f"Executing transfer of {amount} to {address}")

if __name__ == '__main__':
    mock_queue = [
        {'address': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F', 'amount': 1.5},
        {'address': 'invalid_address', 'amount': 0.1}
    ]
    process_transactions(mock_queue)