class WalletError(Exception):
    """Base exception for wallet-utility-83 operations."""

class TransactionError(WalletError):
    """Raised when transaction signing or broadcast fails."""

class InsufficientFundsError(TransactionError):
    """Raised when wallet balance is lower than transaction cost."""

class NetworkTimeoutError(WalletError):
    """Raised during RPC communication timeouts."""

class ConfigurationError(WalletError):
    """Raised when environment or network config is invalid."""

_EXCEPTION_MAP = {
    408: NetworkTimeoutError,
    402: InsufficientFundsError,
}

def get_exception_for_status(status_code: int, default: type = WalletError) -> type:
    """Return mapped exception type for given status code."""
    return _EXCEPTION_MAP.get(status_code, default)

def handle_critical_failure(e: Exception) -> None:
    """Centralized handler for mapping internal exceptions to logs."""
    if isinstance(e, WalletError):
        print(f"[CRITICAL] {e.__class__.__name__}: {str(e)}")
    else:
        print(f"[UNHANDLED] Unexpected error: {str(e)}")