import logging

def is_valid_address(address: str) -> bool:
    """Validates basic crypto address format constraints."""
    return isinstance(address, str) and 26 <= len(address) <= 35 and address.isalnum()

def process_wallet_data(data_list: list):
    """Main loop for processing incoming wallet data chunks."""
    logger = logging.getLogger('wallet-utility-83')
    
    for entry in data_list:
        address = entry.get('address')
        amount = entry.get('amount')

        # Input validation checks
        if not is_valid_address(address):
            logger.error(f'Invalid wallet address detected: {address}')
            continue

        if not isinstance(amount, (int, float)) or amount <= 0:
            logger.error(f'Invalid transaction amount: {amount}')
            continue

        # Proceed with business logic
        try:
            print(f'Processing {amount} for {address}')
            # Transaction processing logic here
        except Exception as e:
            logger.exception('Unexpected processing error')

if __name__ == '__main__':
    sample_data = [
        {'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 'amount': 0.05},
        {'address': 'invalid_addr', 'amount': 0.1},
        {'address': '3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy', 'amount': -5}
    ]
    process_wallet_data(sample_data)