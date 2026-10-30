import re

# Crypto asset constants
SUPPORTED_NETWORKS = {'BTC', 'ETH', 'SOL', 'BSC'}
MIN_TRANSACTION_VALUE = 0.00000001
MAX_TRANSACTION_VALUE = 1000000.0

# Validation patterns
ADDRESS_PATTERN = re.compile(r'^[a-zA-Z0-9]{26,64}$')
TX_HASH_PATTERN = re.compile(r'^0x[a-fA-F0-9]{64}$')

# Error messages
ERR_INVALID_NETWORK = "Network not supported"
ERR_INVALID_AMOUNT = "Transaction amount out of bounds"
ERR_INVALID_FORMAT = "Malformed address or hash format"

def is_valid_address(address: str) -> bool:
    """Validate cryptocurrency address format."""
    return bool(ADDRESS_PATTERN.match(address))

def is_valid_amount(amount: float) -> bool:
    """Ensure amount falls within operational constraints."""
    return MIN_TRANSACTION_VALUE <= amount <= MAX_TRANSACTION_VALUE

def is_valid_network(network: str) -> bool:
    """Verify network against whitelist."""
    return network.upper() in SUPPORTED_NETWORKS