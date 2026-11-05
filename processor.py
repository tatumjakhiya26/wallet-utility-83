import re

def validate_address(address: str) -> bool:
    """Validate cryptocurrency address format."""
    # Basic hex-based validation for generic EVM-style addresses
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def validate_amount(amount: float) -> bool:
    """Ensure transaction amount is positive."""
    return isinstance(amount, (int, float)) and amount > 0

def process_transactions(transactions: list):
    """Main processing loop for wallet transactions."""
    processed_count = 0
    
    for tx in transactions:
        address = tx.get('address')
        amount = tx.get('amount')
        
        # Input validation logic
        if not validate_address(address):
            print(f"Skipping: invalid address format {address}")
            continue
            
        if not validate_amount(amount):
            print(f"Skipping: invalid amount {amount}")
            continue
            
        # Execute logic for valid transactions
        print(f"Processing transaction to {address} for {amount} units")
        processed_count += 1
        
    return processed_count

if __name__ == '__main__':
    data = [
        {'address': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F', 'amount': 1.5},
        {'address': 'invalid_addr', 'amount': 0.5},
        {'address': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F', 'amount': -10}
    ]
    process_transactions(data)