import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "gas_multiplier": 1.2
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with fallback to system defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to parse config file: {e}. Using defaults.")
    
    return config

def get_env_override(key: str, default: Any) -> Any:
    """Fetches configuration from environment variables."""
    return os.getenv(f"WALLET_{key.upper()}", default)

# Initialize primary configuration object
current_config = load_config()

# Apply environment overrides for sensitive fields
for key in current_config:
    current_config[key] = get_env_override(key, current_config[key])