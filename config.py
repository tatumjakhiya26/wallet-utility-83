import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth.llamarpc.com",
    "request_timeout": 30,
    "max_gas_price_gwei": 150,
    "enable_cache": True,
}

class ConfigLoader:
    """Loads configuration with default fallbacks and environment variable overrides."""

    def __init__(self, filepath: str | None = None):
        self.filepath = filepath
        self.settings: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self._load_from_file()
        self._apply_env_overrides()

    def _load_from_file(self) -> None:
        """Attempts to load configuration from a JSON file if it exists."""
        if not self.filepath or not os.path.exists(self.filepath):
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    self.settings.update(data)
        except (json.JSONDecodeError, OSError):
            # Silently fallback to defaults if file is invalid
            pass

    def _apply_env_overrides(self) -> None:
        """Overrides configuration values using WALLET_ env variables."""
        for key, default_value in DEFAULT_CONFIG.items():
            env_key = f"WALLET_{key.upper()}"
            env_value = os.getenv(env_key)
            
            if env_value is not None:
                # Cast the environment variable to match the type of the default value
                target_type = type(default_value)
                try:
                    if target_type is bool:
                        self.settings[key] = env_value.lower() in ("true", "1", "yes", "on")
                    else:
                        self.settings[key] = target_type(env_value)
                except ValueError:
                    # Keep existing value if casting fails
                    pass

    def get(self, key: str) -> Any:
        """Retrieves configuration value by key."""
        return self.settings.get(key, DEFAULT_CONFIG.get(key))