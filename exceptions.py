"""Custom exception hierarchy for wallet operations and edge cases."""

class WalletError(Exception):
    """Base exception class for all crypto wallet operations."""
    def __init__(self, message: str, code: int = 500):
        super().__init__(message)
        self.message = message
        self.code = code


class InvalidAddressError(WalletError):
    """Raised when a crypto wallet address format is invalid."""
    def __init__(self, address: str, network: str = "mainnet"):
        message = f"Invalid {network} address format: '{address}'"
        super().__init__(message, code=400)
        self.address = address
        self.network = network


class InsufficientBalanceError(WalletError):
    """Raised when wallet balance is insufficient for transaction + gas fee."""
    def __init__(self, required: float, available: float, asset: str = "ETH"):
        message = f"Insufficient {asset} balance: required {required}, available {available}"
        super().__init__(message, code=402)
        self.required = required
        self.available = available
        self.asset = asset


class TransactionSigningError(WalletError):
    """Raised when transaction signing fails due to bad key or payload."""
    def __init__(self, reason: str):
        message = f"Failed to sign transaction: {reason}"
        super().__init__(message, code=422)


class NetworkNodeError(WalletError):
    """Raised when RPC/Node communication fails or times out."""
    def __init__(self, node_url: str, details: str):
        message = f"RPC node error [{node_url}]: {details}"
        super().__init__(message, code=503)
        self.node_url = node_url
