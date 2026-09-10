"""
Custom exception hierarchy for the wallet utility.
Provides clear error contexts for crypto transactions, validation, and nodes.
"""

class WalletError(Exception):
    """Base exception for all wallet utility errors."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ValidationError(WalletError):
    """Raised when input validation (addresses, keys, payloads) fails."""
    pass


class InvalidAddressError(ValidationError):
    """Raised when a cryptocurrency address is malformed or invalid."""
    def __init__(self, address: str, network: str, reason: str = "Malformed address"):
        self.address = address
        self.network = network
        super().__init__(f"Invalid {network} address '{address}': {reason}")


class InsufficientFundsError(WalletError):
    """Raised when a wallet lacks enough balance to complete a transaction."""
    def __init__(self, required: float, available: float, currency: str):
        self.required = required
        self.available = available
        self.currency = currency
        super().__init__(
            f"Insufficient funds: required {required} {currency}, "
            f"but only {available} {currency} is available (shortage of {required - available:.8f})"
        )


class NodeConnectionError(WalletError):
    """Raised when connection to the blockchain node fails or times out."""
    def __init__(self, endpoint: str, details: str = ""):
        self.endpoint = endpoint
        suffix = f" Details: {details}" if details else ""
        super().__init__(f"Failed to connect to blockchain node at {endpoint}.{suffix}")
