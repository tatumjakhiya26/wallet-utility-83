"""Custom exception classes for wallet utility operations."""

class WalletError(Exception):
    """Base exception class for all crypto wallet errors."""
    def __init__(self, message: str, code: int = 500):
        super().__init__(message)
        self.message = message
        self.code = code

    def to_dict(self) -> dict:
        """Convert exception details to a dictionary format."""
        return {"error": self.message, "code": self.code}


class InvalidAddressError(WalletError):
    """Raised when a crypto address fails format or checksum validation."""
    def __init__(self, address: str, network: str = "unknown"):
        msg = f"Invalid {network} wallet address format: '{address}'"
        super().__init__(msg, code=400)
        self.address = address
        self.network = network


class InsufficientBalanceError(WalletError):
    """Raised when an account lacks funds for a transaction."""
    def __init__(self, required: float, available: float, symbol: str):
        msg = f"Insufficient {symbol} balance. Required: {required}, Available: {available}"
        super().__init__(msg, code=402)
        self.required = required
        self.available = available
        self.symbol = symbol


class TransactionSigningError(WalletError):
    """Raised when raw transaction signing fails."""
    def __init__(self, details: str):
        super().__init__(f"Failed to sign transaction: {details}", code=422)


class NetworkRPCError(WalletError):
    """Raised when communication with RPC node fails."""
    def __init__(self, endpoint: str, status_code: int = 502):
        super().__init__(f"RPC node failure at {endpoint}", code=status_code)
        self.endpoint = endpoint
