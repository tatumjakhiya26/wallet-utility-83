from typing import Optional

class WalletError(Exception):
    """Base exception class for wallet-utility-83 errors."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class InsufficientFundsError(WalletError):
    """Raised when the wallet balance is too low for the transaction."""
    pass

class NetworkConnectionError(WalletError):
    """Raised when the blockchain node is unreachable."""
    pass

class InvalidAddressError(WalletError):
    """Raised when a provided cryptocurrency address fails checksum validation."""
    pass

class TransactionSigningError(WalletError):
    """Raised when the private key fails to sign the transaction payload."""
    pass

class RateLimitExceededError(WalletError):
    """Raised when API requests exceed defined rate limits."""
    pass