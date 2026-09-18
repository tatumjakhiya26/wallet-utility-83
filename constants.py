import enum

# Network identifiers for blockchain interaction
class NetworkType(enum.Enum):
    MAINNET = "mainnet"
    TESTNET = "testnet"
    DEVNET = "devnet"

# Default gas limit configurations
GAS_LIMIT_TRANSFER = 21000
GAS_LIMIT_CONTRACT = 100000

# Decimal precision for common crypto assets
DECIMALS_ETH = 18
DECIMALS_BTC = 8

# Request timeout settings in seconds
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# Wallet storage encryption parameters
KDF_ITERATIONS = 600000
SALT_SIZE = 16

# Standardized path for key storage
KEYSTORE_PATH = "~/.wallet-utility-83/keystore"

# Supported asset symbols
SUPPORTED_ASSETS = {
    "ETH": "ethereum",
    "BTC": "bitcoin",
    "SOL": "solana"
}

def get_decimals(symbol: str) -> int:
    """Return precision for a given asset symbol."""
    mapping = {"ETH": DECIMALS_ETH, "BTC": DECIMALS_BTC}
    return mapping.get(symbol.upper(), 18)