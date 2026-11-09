import re

# regex patterns for crypto validation
BTC_ADDRESS_REGEX = r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$'
ETH_ADDRESS_REGEX = r'^0x[a-fA-F0-9]{40}$'

def is_valid_address(address: str, chain_type: str) -> bool:
    """
    Validates crypto wallet address format based on network type.
    """
    if not address or not isinstance(address, str):
        return False

    if chain_type == 'BTC':
        return bool(re.match(BTC_ADDRESS_REGEX, address))
    elif chain_type == 'ETH':
        return bool(re.match(ETH_ADDRESS_REGEX, address))
    return False

def validate_amount(amount: float) -> bool:
    """
    Ensures the transaction amount is positive and within logical bounds.
    """
    return isinstance(amount, (int, float)) and amount > 0

def sanitize_input(user_input: str) -> str:
    """
    Basic stripping of input for ledger security.
    """
    return str(user_input).strip()