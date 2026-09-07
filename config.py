import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "rpc_url": "https://api.mainnet-beta.solana.com",
    "timeout": 30,
    "retry_attempts": 3
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """
    Load configuration from file or return defaults if missing.
    """
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

class ConfigError(Exception):
    """
    Custom exception for configuration loading failures.
    """
    pass