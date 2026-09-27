"""Constants for the wallet-utility-83 library.

This module contains configuration defaults, supported networks, BIP44 derivation paths,
and system-wide constants for crypto wallet utilities.
"""

from typing import Dict, Final, Set

# Supported blockchain networks in the utility library
SUPPORTED_NETWORKS: Final[Set[str]] = {"bitcoin", "ethereum", "solana", "polygon"}

# Standard BIP-44 coin type derivation paths
BIP44_PATHS: Final[Dict[str, str]] = {
    "bitcoin": "m/44'/0'/0'/0/0",
    "ethereum": "m/44'/60'/0'/0/0",
    "solana": "m/44'/501'/0'/0'",
    "polygon": "m/44'/966'/0'/0/0",
}

# Number of decimals for the main native assets
DECIMAL_PRECISION: Final[Dict[str, int]] = {
    "BTC": 8,
    "ETH": 18,
    "SOL": 9,
    "MATIC": 18,
}

# Gas fee prioritization tiers and their rate multipliers
GAS_MULTIPLIERS: Final[Dict[str, float]] = {
    "low": 1.0,
    "standard": 1.15,
    "fast": 1.3,
    "instant": 1.5,
}

# Default HTTP client connection timeout in seconds
DEFAULT_TIMEOUT: Final[int] = 30

# Public gateway RPC nodes for supported networks
DEFAULT_RPC_ENDPOINTS: Final[Dict[str, str]] = {
    "ethereum": "https://cloudflare-eth.com",
    "polygon": "https://polygon-rpc.com",
    "solana": "https://api.mainnet-beta.solana.com",
}