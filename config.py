import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "rpc_url": "https://rpc.mainnet.example.com"
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.settings = DEFAULT_CONFIG.copy()
        self._load_from_file()

    def _load_from_file(self) -> None:
        """Loads json configuration from disk if exists."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    file_data = json.load(f)
                    self.settings.update(file_data)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.settings.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self.settings

if __name__ == "__main__":
    # usage demonstration
    loader = ConfigLoader()
    print(f"Loaded network: {loader.get('network')}")