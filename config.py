import os
import json
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging of wallet-utility-83 configuration."""
    
    DEFAULT_CONFIG = {
        "rpc_url": "https://mainnet.infura.io/v3/",
        "timeout": 30,
        "retry_attempts": 3,
        "log_level": "INFO"
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.settings = self.DEFAULT_CONFIG.copy()
        self._load_from_file()

    def _load_from_file(self) -> None:
        """Updates settings if a local configuration file exists."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = json.load(f)
                    self.settings.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a setting by key with fallback."""
        return self.settings.get(key, default)

def get_config() -> ConfigLoader:
    """Factory function for configuration access."""
    return ConfigLoader()