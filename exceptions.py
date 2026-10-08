class WalletError(Exception):
    """Base exception for all wallet operations."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when the wallet balance is too low for the transaction."""
    def __init__(self, required, actual):
        super().__init__(f"Insufficient funds: need {required}, have {actual}")

class InvalidAddressError(WalletError):
    """Raised when a crypto address fails checksum or format validation."""
    pass

class NetworkConnectionError(WalletError):
    """Raised when communication with the blockchain node fails."""
    pass

class TransactionSigningError(WalletError):
    """Raised when local signature generation fails."""
    pass

class RateLimitExceededError(WalletError):
    """Raised when API calls exceed node provider thresholds."""
    pass

def handle_wallet_exception(e: Exception) -> str:
    """Standardized logging and message extraction for UI feedback."""
    if isinstance(e, WalletError):
        return f"[Wallet Error]: {str(e)}"
    return "[Internal System Error]: An unexpected issue occurred."