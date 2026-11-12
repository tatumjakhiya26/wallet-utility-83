import enum

# Network identifiers for blockchain interaction
class NetworkType(enum.Enum):
    MAINNET = "mainnet"
    TESTNET = "testnet"
    DEVNET = "devnet"

# Standardized units for crypto conversion
# Wei values for Ethereum-based operations
WEI_PER_ETH = 10**18
DEFAULT_GAS_LIMIT = 21000

# Validation constraints for address parsing
ADDRESS_LENGTH_HEX = 42
ADDRESS_PREFIX = "0x"

# Timeout settings for network requests
REQUEST_TIMEOUT_SECONDS = 30
MAX_RETRIES = 3

# Common currency precision settings
DEFAULT_DECIMALS = 18

# Map of network endpoints (example structure)
ENDPOINTS = {
    NetworkType.MAINNET: "https://mainnet.infura.io/v3/",
    NetworkType.TESTNET: "https://sepolia.infura.io/v3/"
}

def get_wei_value(amount: float) -> int:
    """Convert ETH float to Wei integer."""
    return int(amount * WEI_PER_ETH)

def is_valid_address(address: str) -> bool:
    """Basic check for address format."""
    return (
        isinstance(address, str) and
        len(address) == ADDRESS_LENGTH_HEX and
        address.startswith(ADDRESS_PREFIX)
    )