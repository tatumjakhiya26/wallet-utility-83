class WalletError(Exception):
    """Base exception for wallet-utility-83 operations."""
    pass

class InsufficientBalanceError(WalletError):
    """Raised when transaction amount exceeds available funds."""
    pass

class InvalidAddressError(WalletError):
    """Raised when a crypto address format is invalid."""
    pass

class NetworkConnectionError(WalletError):
    """Raised when the blockchain node is unreachable."""
    pass

class SecurityAlertError(WalletError):
    """Raised for suspicious activity or auth failures."""
    pass

def handle_wallet_exception(e: Exception) -> str:
    """Format wallet exceptions for logging and user display."""
    if isinstance(e, WalletError):
        return f"[Wallet Error]: {str(e)}"
    return f"[Unexpected Error]: {type(e).__name__} - {str(e)}"