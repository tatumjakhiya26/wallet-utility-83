class WalletError(Exception):
    """Base exception for all wallet operations."""
    pass

class InsufficientFundsError(WalletError):
    """Raised when account balance is too low."""
    def __init__(self, requested: float, available: float):
        self.message = f"Requested {requested} but only {available} available"
        super().__init__(self.message)

class ConnectionTimeoutError(WalletError):
    """Raised when node connection exceeds timeout."""
    pass

class InvalidAddressError(WalletError):
    """Raised for malformed crypto addresses."""
    pass

class TransactionSigningError(WalletError):
    """Raised when transaction signing fails."""
    pass

def raise_if_insufficient(requested: float, balance: float) -> None:
    """Validate balance before executing transactions."""
    if requested > balance:
        raise InsufficientFundsError(requested, balance)

def format_exception(e: Exception) -> str:
    """Convert exception details to loggable string."""
    return f"[{e.__class__.__name__}] {str(e)}"