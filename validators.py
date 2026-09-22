import re

# regex patterns for crypto addresses
ADDRESS_PATTERNS = {
    'BTC': r'^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$',
    'ETH': r'^0x[a-fA-F0-9]{40}$',
    'SOL': r'^[1-9A-HJ-NP-Za-km-z]{32,44}$'
}

def validate_address(address: str, chain: str) -> bool:
    """verify crypto address format against network regex"""
    pattern = ADDRESS_PATTERNS.get(chain.upper())
    if not pattern:
        return False
    return bool(re.match(pattern, address))

def validate_amount(amount: float) -> bool:
    """ensure transaction amount is positive and finite"""
    return isinstance(amount, (int, float)) and amount > 0

def validate_fee(fee: float) -> bool:
    """check fee bounds for network operations"""
    return isinstance(fee, (int, float)) and 0 <= fee < 1.0

def sanitize_memo(memo: str) -> str:
    """strip non-alphanumeric characters from transaction memos"""
    if not memo:
        return ""
    return re.sub(r'[^a-zA-Z0-9 ]', '', memo)[:64]