import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "gas_buffer": 0.001
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads application configuration with fallback defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(path):
        return config
        
    try:
        with open(path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def get_setting(key: str, default_val: Any = None) -> Any:
    """Helper to retrieve single setting from config."""
    config = load_config()
    return config.get(key, default_val)
