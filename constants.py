from typing import Final, Dict

# Network identifier constants
MAINNET: Final[str] = "mainnet"
TESTNET: Final[str] = "testnet"

# Minimum requirement thresholds for wallet validation
MIN_PASSWORD_LENGTH: Final[int] = 12
GAS_LIMIT_DEFAULT: Final[int] = 21000

# Map of crypto asset codes to their respective decimals
ASSET_DECIMALS: Final[Dict[str, int]] = {
    "BTC": 8,
    "ETH": 18,
    "USDT": 6,
    "SOL": 9
}

# API request configuration
TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Default derivation path for standard BIP32 wallets
DEFAULT_DERIVATION_PATH: Final[str] = "m/44'/60'/0'/0/0"

def get_asset_precision(symbol: str) -> int:
    """Return decimal precision for a specific asset symbol."""
    return ASSET_DECIMALS.get(symbol.upper(), 18)

# Application-wide environment configuration
SUPPORTED_NETWORKS: Final[tuple] = (MAINNET, TESTNET)
ENVIRONMENT_FLAGS: Final[Dict[str, bool]] = {
    "DEBUG": False,
    "STRICT_MODE": True
}