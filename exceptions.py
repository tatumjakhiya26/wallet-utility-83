"""
Custom exceptions for the wallet-utility-83 library.
"""

class WalletError(Exception):
    """Base exception for all wallet-related operations."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class InvalidAddressError(WalletError):
    """Raised when a cryptocurrency address format is invalid."""
    def __init__(self, address: str, network: str):
        self.address = address
        self.network = network
        super().__init__(f"Invalid address formatting for '{address}' on {network} network")


class InsufficientFundsError(WalletError):
    """Raised when a transaction's cost exceeds the available wallet balance."""
    def __init__(self, required: float, available: float, asset: str):
        self.required = required
        self.available = available
        self.asset = asset
        super().__init__(
            f"Insufficient balance for {asset}: required {required}, but only {available} available"
        )


class TransactionSigningError(WalletError):
    """Raised when there is a failure during the cryptographic signing process."""
    def __init__(self, details: str):
        super().__init__(f"Failed to sign transaction: {details}")


class NodeConnectionError(WalletError):
    """Raised when the wallet utility cannot communicate with the blockchain node."""
    def __init__(self, endpoint: str, inner_exception: Exception = None):
        self.endpoint = endpoint
        self.inner_exception = inner_exception
        msg = f"Failed to establish connection with node at {endpoint}"
        if inner_exception:
            msg += f" (Reason: {str(inner_exception)})"
        super().__init__(msg)
