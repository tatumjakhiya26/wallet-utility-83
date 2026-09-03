import os
import re
from typing import Dict, Any


class ConfigError(Exception):
    """Custom exception raised for configuration loading errors."""
    pass


class WalletConfig:
    """Manages configuration settings and validates edge cases for wallet utility."""

    SUPPORTED_NETWORKS = {"mainnet", "testnet", "devnet"}

    def __init__(self) -> None:
        self.network: str = os.getenv("CRYPTO_NETWORK", "mainnet").lower()
        self.rpc_url: str = os.getenv("RPC_URL", "https://localhost:8545")
        self.timeout: int = self._parse_timeout(os.getenv("REQUEST_TIMEOUT", "30"))
        self.validate()

    def _parse_timeout(self, timeout_str: str) -> int:
        try:
            val = int(timeout_str)
            if val <= 0:
                raise ValueError("Timeout must be a positive integer.")
            return val
        except ValueError as err:
            raise ConfigError(f"Invalid timeout value '{timeout_str}': {err}") from err

    def validate(self) -> None:
        if self.network not in self.SUPPORTED_NETWORKS:
            allowed = ", ".join(sorted(self.SUPPORTED_NETWORKS))
            raise ConfigError(f"Unsupported network '{self.network}'. Must be one of: {allowed}")

        url_pattern = re.compile(r"^https?://[^\s/$.?#].[^\s]*$", re.IGNORECASE)
        if not url_pattern.match(self.rpc_url):
            raise ConfigError(f"Malformed RPC URL provided: '{self.rpc_url}'")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "network": self.network,
            "rpc_url": self.rpc_url,
            "timeout": self.timeout,
        }
