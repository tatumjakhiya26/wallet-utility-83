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
    """Loads configuration from disk with fallback defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            print(f"Warning: failed to load {path}, using defaults")
            
    return config

def get_setting(key: str, default: Any = None) -> Any:
    """Fetches specific setting from active configuration."""
    config = load_config()
    return config.get(key, default)