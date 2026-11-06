import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "log_level": "INFO"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallbacks to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load {config_path}: {e}")
            
    return config

# Global config instance for application-wide access
app_config = load_config()