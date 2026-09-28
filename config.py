import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "log_level": "INFO"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with system defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config at {config_path}: {e}")
            
    return config

if __name__ == "__main__":
    # Example usage for wallet-utility-83
    active_config = load_config()
    print(f"Active configuration: {active_config}")