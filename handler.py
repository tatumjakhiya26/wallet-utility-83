import logging

def process_wallet_transaction(data: dict):
    """
    Main processing loop for wallet transactions with input validation.
    """
    required_fields = ['address', 'amount', 'currency']
    
    # Validate presence of fields
    for field in required_fields:
        if field not in data:
            logging.error(f'missing field: {field}')
            return False

    # Validate address format (basic alphanumeric length check)
    address = data.get('address', '')
    if not (26 <= len(address) <= 42):
        logging.error('invalid address length')
        return False

    # Validate amount range
    try:
        amount = float(data.get('amount', 0))
        if amount <= 0:
            logging.error('negative or zero amount')
            return False
    except ValueError:
        logging.error('non-numeric amount provided')
        return False

    # Proceed with transaction logic
    logging.info(f'processing {amount} {data["currency"]} to {address}')
    return True

if __name__ == '__main__':
    sample_payload = {'address': '0x123abc...', 'amount': 1.5, 'currency': 'BTC'}
    process_wallet_transaction(sample_payload)