import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "rpc_timeout": 30,
    "retry_attempts": 3,
    "cache_enabled": True
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load config file: {e}. Using defaults.")
    
    return config

if __name__ == "__main__":
    # Example usage for wallet-utility-83
    cfg = load_config()
    print(f"Loaded network: {cfg.get('network')}")