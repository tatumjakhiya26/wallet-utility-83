import enum

class WalletError(enum.Enum):
    """Standardized error identifiers for wallet operations."""
    INSUFFICIENT_FUNDS = "ERR_001"
    INVALID_ADDRESS = "ERR_002"
    NETWORK_TIMEOUT = "ERR_003"
    TRANSACTION_REJECTED = "ERR_004"
    DATABASE_LOCK_FAILURE = "ERR_005"

# Network and transaction configuration constants
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30
MIN_CONFIRMATIONS = 6

# HTTP status codes for external RPC calls
HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_SERVICE_UNAVAILABLE = 503

# Error mapping for user-facing messaging
ERROR_MESSAGES = {
    WalletError.INSUFFICIENT_FUNDS: "Account balance below required transaction amount.",
    WalletError.INVALID_ADDRESS: "The provided wallet address format is invalid.",
    WalletError.NETWORK_TIMEOUT: "Connection to RPC node timed out.",
    WalletError.TRANSACTION_REJECTED: "Transaction was declined by the network.",
    WalletError.DATABASE_LOCK_FAILURE: "System is currently busy processing another write."
}