import re

ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

def validate_address(address: str) -> bool:
    """Verify ethereum-style address format."""
    return bool(ADDRESS_PATTERN.match(address))

def process_wallet_data(wallet_list: list):
    """Main processing loop with input validation."""
    valid_wallets = []
    
    for entry in wallet_list:
        address = entry.get('address')
        amount = entry.get('amount')
        
        # Validation logic
        if not isinstance(address, str) or not validate_address(address):
            print(f'Skipping invalid address: {address}')
            continue
            
        if not isinstance(amount, (int, float)) or amount < 0:
            print(f'Skipping invalid amount: {amount}')
            continue
            
        # Process sanitized data
        valid_wallets.append({'address': address.lower(), 'amount': float(amount)})
        
    return valid_wallets

if __name__ == '__main__':
    data = [
        {'address': '0x1234567890123456789012345678901234567890', 'amount': 1.5},
        {'address': 'invalid_address', 'amount': 10},
        {'address': '0xABCDEF1234567890ABCDEF1234567890ABCDEF12', 'amount': -5}
    ]
    results = process_wallet_data(data)
    print(f'Processed {len(results)} valid wallets.')