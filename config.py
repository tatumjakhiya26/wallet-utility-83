import os
from typing import Any, Dict

# Default configuration for wallet-utility-83
DEFAULT_CONFIG = {
    "RPC_URL": "https://mainnet.infura.io/v3/",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "DEBUG": False
}

def load_config() -> Dict[str, Any]:
    """
    Loads configuration from environment variables with 
    fallback to default settings.
    """
    config = DEFAULT_CONFIG.copy()
    
    # Override defaults with environment variables if present
    for key in config.keys():
        env_val = os.getenv(f"WALLET_{key}")
        if env_val:
            # Handle type conversion for non-string defaults
            default_type = type(config[key])
            try:
                config[key] = default_type(env_val)
            except ValueError:
                continue
                
    return config

# Global config instance for application-wide use
settings = load_config()