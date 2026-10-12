class WalletError(Exception):
    """Base exception for all wallet-utility-83 errors."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when transaction amount exceeds balance."""
    pass

class InvalidAddressError(WalletError):
    """Raised when the destination address is malformed."""
    pass

class ConnectionTimeoutError(WalletError):
    """Raised when node connectivity times out."""
    pass

class SigningError(WalletError):
    """Raised during cryptographic signing failures."""
    pass

class RateLimitError(WalletError):
    """Raised when API requests exceed threshold."""
    pass