from typing import Dict

# Crypto currency network identifiers
MAINNET = 'mainnet'
TESTNET = 'testnet'

# Standardized decimal precision for calculations
DEFAULT_PRECISION = 8

# Gas limit thresholds for common transaction types
GAS_LIMIT_TRANSFER = 21000
GAS_LIMIT_CONTRACT = 100000

# Dictionary of network configuration defaults
NETWORK_CONFIGS: Dict[str, dict] = {
    MAINNET: {
        'chain_id': 1,
        'explorer': 'https://etherscan.io',
        'timeout': 30
    },
    TESTNET: {
        'chain_id': 11155111,
        'explorer': 'https://sepolia.etherscan.io',
        'timeout': 60
    }
}

# Security constants
MIN_PASSWORD_LENGTH = 12
MAX_RETRY_ATTEMPTS = 3