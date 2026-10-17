import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "cache_enabled": True
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file with fallback to defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Configuration load error: {e}, using defaults")
            
    return config

def get_setting(key: str, default: Any = None) -> Any:
    """
    Retrieves a single setting value from the global configuration.
    """
    cfg = load_config()
    return cfg.get(key, default)

if __name__ == "__main__":
    # Example usage for wallet-utility-83
    settings = load_config()
    print(f"Loaded network: {settings.get('network')}")