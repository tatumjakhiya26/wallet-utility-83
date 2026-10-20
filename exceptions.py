class WalletBaseError(Exception):
    """Base exception for all wallet operations."""
    pass

class TransactionExecutionError(WalletBaseError):
    """Raised when transaction signing or broadcast fails."""
    pass

class InsufficientFundsError(WalletBaseError):
    """Raised when account balance is too low."""
    pass

class RateLimitExceeded(WalletBaseError):
    """Raised when API requests exceed threshold."""
    def __init__(self, retry_after: int):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry in {retry_after}s.")

class ValidationError(WalletBaseError):
    """Raised when input validation fails."""
    pass

def handle_wallet_exception(e: Exception) -> dict:
    """Standardizes exception output for logs and UI."""
    if isinstance(e, RateLimitExceeded):
        return {"error": "rate_limited", "retry_after": e.retry_after}
    
    return {"error": "internal_failure", "message": str(e)}

# Custom exception groups for parallel process batching
class BatchProcessingError(WalletBaseError):
    """Collection of errors during multi-transaction execution."""
    def __init__(self, errors: list):
        self.errors = errors
        super().__init__(f"Batch processing failed with {len(errors)} errors")