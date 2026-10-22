import os

# Network constants for wallet-utility-83
SUPPORTED_NETWORKS = {
    'mainnet': 'https://mainnet.infura.io/v3/',
    'sepolia': 'https://sepolia.infura.io/v3/',
    'bsc': 'https://bsc-dataseed.binance.org/'
}

# Transaction configurations
DEFAULT_GAS_LIMIT = 21000
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# Currency units
WEI_PER_ETHER = 10**18
GWEI_PER_ETHER = 10**9

# Security configurations
MIN_PASSWORD_LENGTH = 12
ENCRYPTION_ITERATIONS = 100000

# Environment setup
LOG_LEVEL = os.getenv('WALLET_LOG_LEVEL', 'INFO')
STORAGE_PATH = os.path.join(os.path.expanduser('~'), '.wallet-utility-83')