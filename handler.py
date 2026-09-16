import re

def validate_address(address: str) -> bool:
    """Validates Ethereum-like wallet address format."""
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def validate_amount(amount: float) -> bool:
    """Ensures transaction amount is positive and non-zero."""
    return isinstance(amount, (int, float)) and amount > 0

def process_transactions(queue):
    """
    Main processing loop with input validation
    for wallet-utility-83 pipeline.
    """
    processed = []
    for tx in queue:
        addr = tx.get('address')
        amt = tx.get('amount')

        if not validate_address(addr):
            print(f'Skipping: Invalid address format {addr}')
            continue

        if not validate_amount(amt):
            print(f'Skipping: Invalid amount {amt}')
            continue

        # Execute transaction logic here
        processed.append({'address': addr, 'amount': amt, 'status': 'success'})
        print(f'Processed tx for {addr}')
    
    return processed