class WalletError(Exception):
    """Base exception for wallet-utility-83 operations."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when account balance is too low."""
    pass

class ConnectionTimeoutError(WalletError):
    """Raised when network requests fail."""
    pass

class InvalidAddressError(WalletError):
    """Raised when wallet address format is incorrect."""
    pass

class TransactionSigningError(WalletError):
    """Raised during cryptographic signing failures."""
    pass

class RateLimitExceededError(WalletError):
    """Raised when API thresholds are breached."""
    pass

def handle_wallet_exception(err: Exception) -> str:
    """Format custom wallet exceptions for logging."""
    if isinstance(err, WalletError):
        return f"[Wallet Error] {type(err).__name__}: {str(err)}"
    return f"[Unexpected Error] {str(err)}"