import json
import os
from typing import Any, Dict

# Default settings for the crypto wallet utility
DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "timeout_seconds": 30,
    "max_retries": 3,
    "gas_price_multiplier": 1.1,
    "enable_metrics": False,
    "log_level": "INFO",
    "cache_ttl_seconds": 300,
}


class ConfigLoader:
    """Loads configuration settings with default fallback and env overrides."""

    def __init__(self, config_path: str | None = None):
        self.config_path = config_path or os.getenv("WALLET_CONFIG_PATH", "config.json")
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Load config from JSON file if present and apply environment overrides."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    self._config.update(file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load config file {self.config_path}: {err}")

        self._apply_env_overrides()
        return self._config

    def _apply_env_overrides(self) -> None:
        """Override configuration options using WALLET_ environment variables."""
        prefix = "WALLET_"
        for key, default_val in DEFAULT_CONFIG.items():
            env_var = prefix + key.upper()
            if env_var in os.environ:
                raw_val = os.environ[env_var]
                val_type = type(default_val)
                if val_type == bool:
                    self._config[key] = raw_val.lower() in ("true", "1", "yes")
                elif val_type in (int, float):
                    try:
                        self._config[key] = val_type(raw_val)
                    except ValueError:
                        pass
                else:
                    self._config[key] = raw_val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    @property
    def config(self) -> Dict[str, Any]:
        """Return a copy of the active configuration dictionary."""
        return self._config.copy()
