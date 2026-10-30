import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "request_timeout": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.15,
    "cache_ttl_seconds": 300,
    "enable_telemetry": False,
    "log_level": "INFO",
}


class ConfigLoader:
    """Loads and manages configuration for wallet utility operations."""

    def __init__(self, config_path: str | None = None) -> None:
        self.config_path = Path(config_path) if config_path else None
        self._config = DEFAULT_CONFIG.copy()
        self.reload()

    def _load_from_file(self) -> Dict[str, Any]:
        """Reads configuration options from a JSON file if present."""
        if not self.config_path or not self.config_path.exists():
            return {}
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}

    def _load_from_env(self) -> Dict[str, Any]:
        """Overrides configuration settings using environment variables."""
        env_mappings = {
            "WALLET_NETWORK": ("network", str),
            "WALLET_RPC_URL": ("rpc_url", str),
            "WALLET_TIMEOUT": ("request_timeout", int),
            "WALLET_MAX_RETRIES": ("max_retries", int),
            "WALLET_LOG_LEVEL": ("log_level", str),
        }
        overrides = {}
        for env_var, (key, cast_type) in env_mappings.items():
            val = os.getenv(env_var)
            if val is not None:
                try:
                    overrides[key] = cast_type(val)
                except ValueError:
                    pass
        return overrides

    def reload(self) -> None:
        """Reloads configuration combining defaults, file settings, and env vars."""
        file_opts = self._load_from_file()
        env_opts = self._load_from_env()
        self._config = {**DEFAULT_CONFIG, **file_opts, **env_opts}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration parameter by key."""
        return self._config.get(key, default)

    @property
    def current(self) -> Dict[str, Any]:
        """Returns a copy of the current effective configuration."""
        return self._config.copy()
