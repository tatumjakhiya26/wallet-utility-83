class WalletError(Exception):
    """Base exception class for wallet operations."""
    pass

class InsufficientBalanceError(WalletError):
    """Raised when transaction amount exceeds available funds."""
    def __init__(self, requested: float, available: float):
        super().__init__(f"Insufficient funds: requested {requested}, available {available}")

class InvalidAddressError(WalletError):
    """Raised when a crypto address format is invalid."""
    def __init__(self, address: str, chain: str):
        super().__init__(f"Invalid {chain} address format: {address}")

class ConnectionTimeoutError(WalletError):
    """Raised when node communication fails."""
    def __init__(self, node: str):
        super().__init__(f"Connection to node {node} timed out")

class SigningError(WalletError):
    """Raised during transaction signing process."""
    def __init__(self, reason: str):
        super().__init__(f"Transaction signing failed: {reason}")