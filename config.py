import os
import json
from typing import Dict, Any, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "chain_id": 1,
    "gas_limit_multiplier": 1.15,
    "request_timeout": 30,
    "max_retries": 3,
    "enable_metrics": False,
    "cache_ttl_seconds": 300,
}


class ConfigManager:
    """Manages application configuration loading and fallback to defaults."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self._load()

    def _load(self) -> None:
        # Overwrite defaults with file configuration if provided and exists
        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self._config.update(file_config)
            except (json.JSONDecodeError, OSError):
                pass  # Fall back to defaults on read error

        # Environment variables take precedence over file and defaults
        env_rpc = os.getenv("WALLET_RPC_URL")
        if env_rpc:
            self._config["rpc_url"] = env_rpc

        env_network = os.getenv("WALLET_NETWORK")
        if env_network:
            self._config["network"] = env_network

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def as_dict(self) -> Dict[str, Any]:
        """Return a copy of the active configuration dictionary."""
        return self._config.copy()
