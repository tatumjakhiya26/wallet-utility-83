from typing import Optional

class WalletError(Exception):
    """Base exception for all wallet-utility-83 errors."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class InsufficientFundsError(WalletError):
    """Raised when the wallet balance is too low for the transaction."""
    def __init__(self, balance: float, required: float) -> None:
        message = f"Insufficient balance: have {balance}, need {required}"
        super().__init__(message, code=1001)

class InvalidAddressError(WalletError):
    """Raised when the provided cryptocurrency address is malformed."""
    def __init__(self, address: str) -> None:
        message = f"Invalid format for address: {address}"
        super().__init__(message, code=1002)

class ConnectionTimeoutError(WalletError):
    """Raised when the blockchain node fails to respond in time."""
    def __init__(self, endpoint: str) -> None:
        message = f"Timeout connecting to endpoint: {endpoint}"
        super().__init__(message, code=1003)

class SignatureError(WalletError):
    """Raised when transaction signing fails due to bad keys."""
    def __init__(self, reason: str) -> None:
        message = f"Transaction signature failed: {reason}"
        super().__init__(message, code=1004)