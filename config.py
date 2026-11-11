import os
import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "chain_id": 1,
    "request_timeout": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.15,
    "data_dir": str(Path.home() / ".wallet_utility"),
    "enable_metrics": False,
}

class WalletConfig:
    """Manages application settings with environment overrides and fallback defaults."""

    def __init__(self, config_dict: Dict[str, Any] = None):
        self._settings = DEFAULT_CONFIG.copy()
        if config_dict:
            self._settings.update(config_dict)
        self._load_env_overrides()

    def _load_env_overrides(self) -> None:
        """Override configuration values using defined environment variables."""
        env_mappings = {
            "WALLET_NETWORK": ("network", str),
            "WALLET_RPC_URL": ("rpc_url", str),
            "WALLET_CHAIN_ID": ("chain_id", int),
            "WALLET_TIMEOUT": ("request_timeout", int),
            "WALLET_DATA_DIR": ("data_dir", str),
        }
        for env_var, (key, type_cast) in env_mappings.items():
            val = os.getenv(env_var)
            if val is not None:
                try:
                    self._settings[key] = type_cast(val)
                except ValueError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key."""
        return self._settings.get(key, default)

    @classmethod
    def load_from_file(cls, filepath: str) -> "WalletConfig":
        """Load configuration settings from a JSON file."""
        path = Path(filepath)
        if not path.is_file():
            return cls()
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(data)

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of current active settings."""
        return self._settings.copy()
