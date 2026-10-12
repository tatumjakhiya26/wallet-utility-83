from typing import Final

# Configuration constants for wallet-utility-83
# All values are strictly typed and immutable

MIN_TX_AMOUNT: Final[float] = 0.00000001
MAX_TX_AMOUNT: Final[float] = 1000000.0
DEFAULT_TIMEOUT: Final[int] = 30

# Currency network identifiers
NETWORKS: Final[dict[str, str]] = {
    "BTC": "mainnet",
    "ETH": "homestead",
    "SOL": "mainnet-beta"
}

# Error handling status codes
ERR_INSUFFICIENT_FUNDS: Final[str] = "ERR_001"
ERR_INVALID_ADDRESS: Final[str] = "ERR_002"
ERR_NETWORK_TIMEOUT: Final[str] = "ERR_003"
ERR_RATE_LIMIT: Final[str] = "ERR_004"

# Supported validation patterns
ADDRESS_PATTERNS: Final[dict[str, str]] = {
    "BTC": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$",
    "ETH": r"^0x[a-fA-F0-9]{40}$",
    "SOL": r"^[1-9A-HJ-NP-Za-km-z]{32,44}$"
}

# Utility constants for retry mechanisms
MAX_RETRIES: Final[int] = 3
BACKOFF_FACTOR: Final[float] = 1.5