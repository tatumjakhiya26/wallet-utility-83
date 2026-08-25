import hashlib
import re
from typing import Any, Dict

def validate_ethereum_address(address: str) -> bool:
    """Validate an Ethereum address format."""
    if not isinstance(address, str):
        return False
    if not address.startswith("0x"):
        return False
    if len(address) != 42:
        return False
    return bool(re.match(r"^[0-9a-fA-F]+$", address[2:]))

def wei_to_eth(wei: int) -> float:
    """Convert wei amount to ETH."""
    if not isinstance(wei, int) or wei < 0:
        raise ValueError("Wei must be a non-negative integer")
    return wei / (10 ** 18)

def eth_to_wei(eth: float) -> int:
    """Convert ETH to wei."""
    if not isinstance(eth, (int, float)) or eth < 0:
        raise ValueError("ETH amount must be non-negative")
    return int(eth * (10 ** 18))

def format_crypto_amount(amount: float, symbol: str = "ETH", decimals: int = 6) -> str:
    """Format a crypto amount for display."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    formatted = f"{amount:.{decimals}f}"
    return f"{formatted} {symbol}"

def calculate_data_hash(data: Dict[str, Any]) -> str:
    """Calculate SHA256 hash for given data dictionary."""
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")
    sorted_data = sorted(data.items())
    data_str = str(sorted_data).encode("utf-8")
    return hashlib.sha256(data_str).hexdigest()

def normalize_balance_data(raw_data: Dict[str, Any]) -> Dict[str, float]:
    """Normalize various crypto balance response formats."""
    if not raw_data or not isinstance(raw_data, dict):
        return {}
    normalized = {}
    for asset, info in raw_data.items():
        if isinstance(info, (int, float)):
            normalized[asset] = float(info)
        elif isinstance(info, dict):
            balance = info.get("balance", 0)
            try:
                bal = float(balance)
                if "decimals" in info:
                    bal /= (10 ** int(info["decimals"]))
                normalized[asset] = bal
            except (ValueError, TypeError):
                normalized[asset] = 0.0
    return normalized