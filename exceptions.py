class WalletError(Exception):
    """Base exception for wallet-utility-83 operations."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when transaction amount exceeds available balance."""
    pass

class InvalidAddressError(WalletError):
    """Raised when a crypto address format is invalid."""
    pass

class NetworkTimeoutError(WalletError):
    """Raised when node connection times out."""
    pass

class SigningError(WalletError):
    """Raised when cryptographic signing fails."""
    pass

class ConfigError(WalletError):
    """Raised for issues in environment or configuration loading."""
    pass