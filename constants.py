from typing import Final, Dict, List

# Configuration constants for wallet-utility-83

MIN_CONFIRMATIONS: Final[int] = 6
MAX_GAS_LIMIT: Final[int] = 500000

SUPPORTED_NETWORKS: Final[List[str]] = [
    "mainnet",
    "testnet",
    "sepolia"
]

DEFAULT_TIMEOUT: Final[float] = 30.0

NETWORK_RPC_URLS: Final[Dict[str, str]] = {
    "mainnet": "https://mainnet.infura.io/v3/",
    "testnet": "https://goerli.infura.io/v3/",
    "sepolia": "https://sepolia.infura.io/v3/"
}

ERROR_MESSAGES: Final[Dict[str, str]] = {
    "insufficient_funds": "Address lacks balance for this transaction",
    "invalid_address": "Provided address format is unsupported",
    "network_timeout": "Remote node connection timed out"
}

def get_rpc_url(network: str) -> str:
    """Return RPC URL for a given network name."""
    return NETWORK_RPC_URLS.get(network, "")