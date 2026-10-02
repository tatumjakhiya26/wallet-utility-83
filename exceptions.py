class CryptoBaseException(Exception):
    """Base exception for wallet-utility-83 errors."""
    pass

class InsufficientFundsError(CryptoBaseException):
    """Raised when wallet balance is below transaction requirement."""
    def __init__(self, required: float, actual: float):
        self.message = f"Required {required} but only {actual} available"
        super().__init__(self.message)

class TransactionValidationError(CryptoBaseException):
    """Raised when transaction parameters are malformed."""
    pass

class NetworkConnectionError(CryptoBaseException):
    """Raised when blockchain node is unreachable."""
    def __init__(self, endpoint: str):
        self.message = f"Failed to establish connection to {endpoint}"
        super().__init__(self.message)

class RateLimitExceeded(CryptoBaseException):
    """Raised when API request frequency exceeds constraints."""
    pass

class KeyManagementError(CryptoBaseException):
    """Raised during failure to sign or decrypt keys."""
    pass