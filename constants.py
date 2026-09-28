from typing import Final

# Configuration constants for wallet-utility-83 core engine
# Optimized using cached lookups and finalized types

CACHE_TTL_SECONDS: Final[int] = 300
MAX_RETRIES: Final[int] = 3
NETWORK_TIMEOUT: Final[float] = 10.5

# Supported cryptocurrency network identifiers
NETWORKS: Final[dict[str, str]] = {
    'BTC': 'bitcoin',
    'ETH': 'ethereum',
    'SOL': 'solana',
    'ADA': 'cardano'
}

# Batch processing thresholds to minimize network overhead
BATCH_SIZE_LIMIT: Final[int] = 50
REQUEST_INTERVAL_MS: Final[int] = 100

# Precision constants for financial calculations
DECIMAL_PRECISION: Final[int] = 18
DEFAULT_GAS_LIMIT: Final[int] = 21000

def get_network_name(ticker: str) -> str:
    """Return full network name with fallback for unknown tickers."""
    return NETWORKS.get(ticker.upper(), 'unknown')