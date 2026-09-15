from enum import Enum

class WalletErrorCodes(Enum):
    INSUFFICIENT_FUNDS = "ERR_001"
    INVALID_ADDRESS = "ERR_002"
    NETWORK_TIMEOUT = "ERR_003"
    DECRYPTION_FAILED = "ERR_004"
    UNSUPPORTED_ASSET = "ERR_005"

ERROR_MESSAGES = {
    WalletErrorCodes.INSUFFICIENT_FUNDS: "Insufficient balance for transaction requirements",
    WalletErrorCodes.INVALID_ADDRESS: "The provided wallet address format is invalid",
    WalletErrorCodes.NETWORK_TIMEOUT: "Connection to blockchain node timed out",
    WalletErrorCodes.DECRYPTION_FAILED: "Failed to unlock wallet with provided credentials",
    WalletErrorCodes.UNSUPPORTED_ASSET: "Transaction currency not supported by current chain"
}

MAX_RETRIES = 3
DEFAULT_TIMEOUT_SECONDS = 30.0

def get_error_message(code: WalletErrorCodes) -> str:
    """Return user-friendly error message for a specific code."""
    return ERROR_MESSAGES.get(code, "An unknown wallet error occurred")