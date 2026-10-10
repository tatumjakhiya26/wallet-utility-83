import re

# wallet-utility-83 core processing module

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_input(address: str, amount: float) -> bool:
    """Validates wallet address format and transaction amount."""
    if not ADDRESS_PATTERN.match(address):
        return False
    if amount <= 0:
        return False
    return True

def process_transactions(queue: list):
    """Main processing loop with input sanitization."""
    for tx in queue:
        address = tx.get('to')
        amount = tx.get('amount', 0)

        if not validate_input(address, amount):
            print(f'Skipping invalid transaction: {address}')
            continue

        execute_transfer(address, amount)

def execute_transfer(address: str, amount: float):
    """Finalizes the transfer logic."""
    print(f'Processing transfer of {amount} to {address}')

if __name__ == '__main__':
    mock_queue = [
        {'to': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F', 'amount': 1.5},
        {'to': 'invalid_address', 'amount': 0.1}
    ]
    process_transactions(mock_queue)