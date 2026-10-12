import re
from typing import Dict, Any

def validate_address(address: str) -> bool:
    # Matches standard hex-encoded crypto addresses
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

def process_transaction(data: Dict[str, Any]) -> None:
    """
    Main processing loop for incoming crypto wallet requests.
    Ensures input integrity before blockchain execution.
    """
    required_fields = ['address', 'amount']
    
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')

    address = data['address']
    amount = data['amount']

    if not validate_address(address):
        raise ValueError(f'Invalid blockchain address format: {address}')

    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError('Amount must be a positive numeric value')

    # Proceed with transaction logic
    print(f'Processing transfer of {amount} to {address}')

if __name__ == '__main__':
    sample_payload = {'address': '0x1234567890123456789012345678901234567890', 'amount': 1.5}
    try:
        process_transaction(sample_payload)
    except ValueError as e:
        print(f'Validation failed: {e}')