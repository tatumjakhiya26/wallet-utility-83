class WalletError(Exception):
    """Base exception for wallet-utility-83 operations."""
    pass

class InsufficientBalanceError(WalletError):
    """Raised when transaction amount exceeds available balance."""
    def __init__(self, required, available):
        self.message = f"Required {required} but only {available} available"
        super().__init__(self.message)

class ConnectionTimeoutError(WalletError):
    """Raised when node connectivity fails after retries."""
    pass

class ValidationError(WalletError):
    """Raised when input parameters fail address or format checks."""
    pass

class SigningError(WalletError):
    """Raised when cryptographic signing process fails."""
    pass