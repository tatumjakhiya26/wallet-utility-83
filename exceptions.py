from typing import Optional

class WalletError(Exception):
    """Base exception class for wallet-utility-83 errors."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class InsufficientFundsError(WalletError):
    """Raised when the wallet balance is too low for the transaction."""
    pass

class ConnectionTimeoutError(WalletError):
    """Raised when the node connection times out."""
    pass

class InvalidAddressError(WalletError):
    """Raised when a provided crypto address format is invalid."""
    def __init__(self, address: str) -> None:
        super().__init__(f"Invalid address format provided: {address}", code=400)

class TransactionSigningError(WalletError):
    """Raised when the signing process fails due to invalid keys."""
    pass

class ConfigurationError(WalletError):
    """Raised when application settings are missing or misconfigured."""
    pass