import os
from typing import Final
from functools import lru_cache

# Configuration constants for wallet-utility-83
# Using lru_cache for frequent lookups to reduce memory overhead

CACHE_SIZE: Final[int] = 128
DEFAULT_TIMEOUT: Final[float] = 30.0
MAX_RETRIES: Final[int] = 3

# Supported network identifiers
NETWORKS: Final[dict[str, str]] = {
    "mainnet": "https://mainnet.infura.io/v3/",
    "testnet": "https://sepolia.infura.io/v3/",
}

@lru_cache(maxsize=CACHE_SIZE)
def get_rpc_endpoint(network: str) -> str:
    """Retrieves cached RPC endpoint for given network."""
    base_url = NETWORKS.get(network)
    if not base_url:
        raise ValueError(f"Unsupported network: {network}")
    
    api_key = os.getenv("RPC_API_KEY", "default_key")
    return f"{base_url}{api_key}"

# Fee estimation constants
GAS_PRICE_MULTIPLIER: Final[float] = 1.2
MIN_CONFIRMATIONS: Final[int] = 2

# Security threshold definitions
MIN_PASSWORD_LENGTH: Final[int] = 12
MAX_FAILED_ATTEMPTS: Final[int] = 5