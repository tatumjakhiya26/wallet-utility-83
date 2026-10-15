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
    """Loads configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Failed to load config file: {e}. Using defaults.")
            
    return config

def get_rpc_settings() -> Dict[str, Any]:
    """Helper for retrieving crypto-specific network parameters."""
    config = load_config()
    return {
        "url": config.get("rpc_url"),
        "timeout": config.get("timeout"),
        "retries": config.get("retry_attempts")
    }