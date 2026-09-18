import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "gas_buffer": 0.001
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
            print(f"Warning: Could not read config {config_path}: {e}. Using defaults.")
            
    return config

def get_config_value(key: str, default: Any = None) -> Any:
    """Helper to retrieve a single configuration value."""
    config = load_config()
    return config.get(key, default)

if __name__ == "__main__":
    # Example usage for wallet-utility-83
    current_cfg = load_config()
    print(f"Active network: {current_cfg['network']}")