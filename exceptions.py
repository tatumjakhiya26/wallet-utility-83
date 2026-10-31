class WalletError(Exception):
    """Base exception for all wallet-utility-83 errors."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when transaction amount exceeds balance."""
    def __init__(self, required, available):
        super().__init__(f"Required {required}, but only {available} available")

class NetworkConnectionError(WalletError):
    """Raised when the RPC node is unreachable."""
    pass

class InvalidAddressError(WalletError):
    """Raised when the destination address is malformed."""
    pass

class TransactionSigningError(WalletError):
    """Raised when private key signing fails."""
    pass

class ValidationError(WalletError):
    """Raised when input parameters fail schema validation."""
    pass