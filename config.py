import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retry_attempts": 3,
    "log_level": "INFO"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load config file: {e}. Using defaults.")
            
    return config

class ConfigManager:
    """Thread-safe-ish configuration access for wallet operations."""
    def __init__(self, path: str = "config.json"):
        self._data = load_config(path)
        
    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    @property
    def rpc_url(self) -> str:
        return self._data.get("rpc_url", DEFAULT_CONFIG["rpc_url"])
