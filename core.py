import re

# wallet-utility-83 core processing

def validate_address(address: str) -> bool:
    # validate standard bitcoin-style address format
    return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))

def validate_amount(amount: str) -> bool:
    try:
        val = float(amount)
        return val > 0
    except ValueError:
        return False

def run_processor(data_stream: list):
    """Process stream of wallet transactions with input validation."""
    for entry in data_stream:
        address = entry.get('address', '')
        amount = entry.get('amount', '0')

        if not validate_address(address):
            print(f"[ERROR] Invalid address format: {address}")
            continue

        if not validate_amount(amount):
            print(f"[ERROR] Invalid transaction amount: {amount}")
            continue

        # process verified transaction
        print(f"[SUCCESS] Processing {amount} to {address}")

if __name__ == '__main__':
    mock_data = [
        {'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 'amount': '0.5'},
        {'address': 'invalid_addr', 'amount': '0.1'},
        {'address': '3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy', 'amount': '-5'}
    ]
    run_processor(mock_data)