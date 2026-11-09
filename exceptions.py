class WalletError(Exception):
    """Base exception for wallet-utility-83 operations."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when account balance is too low for transaction."""
    pass

class InvalidAddressError(WalletError):
    """Raised when a crypto address format is invalid."""
    pass

class NetworkTimeoutError(WalletError):
    """Raised when the blockchain node fails to respond."""
    pass

class ConfigurationError(WalletError):
    """Raised when required keys or environment variables are missing."""
    pass

class TransactionSigningError(WalletError):
    """Raised when cryptographic signing of a transaction fails."""
    pass

def handle_wallet_exception(err: Exception) -> None:
    """Centralized error reporting utility."""
    if isinstance(err, WalletError):
        print(f"[Wallet Utility Error]: {str(err)}")
    else:
        print(f"[Unexpected System Error]: {str(err)}")