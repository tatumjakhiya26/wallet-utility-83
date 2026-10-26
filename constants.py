from typing import Dict, Final

# Network identifiers for blockchain interaction
NETWORKS: Final[Dict[str, str]] = {
    'mainnet': 'https://mainnet.infura.io/v3/',
    'sepolia': 'https://sepolia.infura.io/v3/',
    'polygon': 'https://polygon-rpc.com',
}

# Standardized unit conversion constants
WEI_PER_ETH: Final[int] = 10**18
SATOSHI_PER_BTC: Final[int] = 10**8

# Precision limits for crypto asset calculations
MAX_DECIMAL_PLACES: Final[int] = 18
DEFAULT_GAS_LIMIT: Final[int] = 21000

# Common currency identifiers
ASSETS: Final[Dict[str, str]] = {
    'BTC': 'Bitcoin',
    'ETH': 'Ethereum',
    'USDT': 'Tether',
    'USDC': 'USD Coin'
}

# Validation bounds for transaction monitoring
MIN_TX_VALUE: Final[float] = 0.00000001
TIMEOUT_SECONDS: Final[int] = 30

def get_network_url(name: str) -> str:
    """Retrieve RPC endpoint for specified network."""
    return NETWORKS.get(name.lower(), 'https://mainnet.infura.io/v3/')