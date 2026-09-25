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
    """Loads configuration from disk with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def get_config_value(key: str, default: Any = None) -> Any:
    """Retrieves specific key from system environment or config."""
    env_val = os.getenv(key.upper())
    if env_val is not None:
        return env_val
    
    config = load_config()
    return config.get(key, default)