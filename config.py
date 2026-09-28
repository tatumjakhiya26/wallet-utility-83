import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retries": 3,
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
            print(f"Warning: Could not load config file: {e}. Using defaults.")
            
    return config

def get_env_overrides(config: Dict[str, Any]) -> Dict[str, Any]:
    """Overwrites config values with environment variables if present."""
    env_mapping = {
        "WALLET_RPC_URL": "rpc_url",
        "WALLET_TIMEOUT": "timeout"
    }
    
    for env_var, config_key in env_mapping.items():
        value = os.getenv(env_var)
        if value:
            config[config_key] = int(value) if value.isdigit() else value
            
    return config