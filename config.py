import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "node_url": "https://api.mainnet.network"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def get_node_config() -> Dict[str, Any]:
    """Utility to fetch active wallet configuration."""
    return load_config()