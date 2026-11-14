"""Centralized constants for crypto wallet operations and chain specifications."""

from typing import Dict, Any

# Supported Blockchain Network Identifiers
CHAIN_IDS: Dict[str, int] = {
    "ethereum": 1,
    "goerli": 5,
    "sepolia": 11155111,
    "polygon": 137,
    "arbitrum": 42161,
    "optimism": 10,
    "bsc": 56,
}

# Standard BIP-44 Derivation Paths
DERIVATION_PATHS: Dict[str, str] = {
    "ethereum": "m/44'/60'/0'/0/0",
    "bitcoin": "m/44'/0'/0'/0/0",
    "solana": "m/44'/501'/0'/0'",
}

# Default RPC Endpoints (Public fallbacks)
DEFAULT_RPC_URLS: Dict[str, str] = {
    "ethereum": "https://eth.llamarpc.com",
    "polygon": "https://polygon-rpc.com",
    "arbitrum": "https://arb1.arbitrum.io/rpc",
    "optimism": "https://mainnet.optimism.io",
    "bsc": "https://bsc-dataseed.binance.org/",
}

# Standard Gas Limits for Ethereum Transactions
DEFAULT_GAS_LIMITS: Dict[str, int] = {
    "eth_transfer": 21000,
    "erc20_transfer": 65000,
    "erc721_transfer": 85000,
    "uniswap_swap": 200000,
}

# Regex Patterns for Address Validation
ADDRESS_PATTERNS: Dict[str, str] = {
    "evm": r"^0x[a-fA-F0-9]{40}$",
    "bitcoin_legacy": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$",
    "bitcoin_bech32": r"^bc1[a-z0-9]{39,59}$",
    "solana": r"^[1-9A-HJ-NP-Za-km-z]{32,44}$",
}


def get_chain_config(network: str) -> Dict[str, Any]:
    """Retrieve full configuration constants for a given network name."""
    net_key = network.lower().strip()
    return {
        "chain_id": CHAIN_IDS.get(net_key),
        "derivation_path": DERIVATION_PATHS.get(net_key),
        "rpc_url": DEFAULT_RPC_URLS.get(net_key),
    }
