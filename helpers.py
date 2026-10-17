import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retry_attempts": 3,
    "log_level": "INFO"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Load configuration from file or return default values.
    """
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: could not load config file: {e}. Using defaults.")
    
    return config

def get_config_value(key: str, default: Any = None) -> Any:
    """
    Fetch specific configuration setting with fallback.
    """
    config = load_config()
    return config.get(key, default)