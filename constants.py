import enum

# Network identifiers for blockchain interaction
class NetworkType(enum.Enum):
    MAINNET = "mainnet"
    TESTNET = "testnet"
    DEVNET = "devnet"

# Standardized unit definitions
SATOSHI_PER_BTC = 10**8
GWEI_PER_ETH = 10**9

# Default timeout values for network requests in seconds
DEFAULT_REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

# Common derivation paths
BIP44_PATH = "m/44'/0'/0'/0/0"

# Validation constraints
MIN_PASSWORD_LENGTH = 12
SUPPORTED_CURRENCIES = {"BTC", "ETH", "USDT", "USDC"}

# Default gas settings
DEFAULT_GAS_LIMIT = 21000
PRIORITY_FEE_MULTIPLIER = 1.2

# Configuration paths
CONFIG_FILE_NAME = "wallet.conf"
STORAGE_DIRECTORY = ".wallet_data"
