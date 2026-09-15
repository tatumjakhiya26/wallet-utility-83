import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "rpc_url": "https://mainnet.infura.io/v3/",
    "retry_attempts": 3,
    "timeout": 30
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Configuration load failed, using defaults: {e}")

    return config

class ConfigLoader:
    """Encapsulated configuration provider for wallet services."""
    def __init__(self, path: str = "config.json"):
        self._data = load_config(path)

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._data.copy()