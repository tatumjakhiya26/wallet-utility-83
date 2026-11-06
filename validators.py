import re

# regex patterns for crypto addresses
ETH_ADDR_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
BTC_ADDR_PATTERN = re.compile(r'^(1|3|bc1)[a-zA-Z0-9]{25,59}$')

def is_valid_address(address: str, chain: str) -> bool:
    """Validate address format for specified chain."""
    if chain.lower() == 'ethereum':
        return bool(ETH_ADDR_PATTERN.match(address))
    if chain.lower() == 'bitcoin':
        return bool(BTC_ADDR_PATTERN.match(address))
    return False

def is_valid_amount(amount: str) -> bool:
    """Validate amount as a positive numeric string."""
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def sanitize_memo(memo: str) -> str:
    """Remove non-alphanumeric chars for transaction memos."""
    return re.sub(r'[^a-zA-Z0-9 ]', '', memo).strip()