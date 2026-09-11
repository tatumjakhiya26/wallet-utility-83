import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "NETWORK": "mainnet",
    "RPC_TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "KEYSTORE_PATH": "./data/keys",
    "ENABLE_AUTO_SYNC": True
}

def load_config(overrides: Dict[str, Any] = None) -> Dict[str, Any]:
    """Merges default configuration with environment variables and manual overrides."""
    config = DEFAULT_CONFIG.copy()
    
    # Check environment variables for config values
    for key in config:
        env_val = os.getenv(f"WALLET_{key}")
        if env_val is not None:
            # Handle type casting for expected types
            if isinstance(config[key], int):
                config[key] = int(env_val)
            elif isinstance(config[key], bool):
                config[key] = env_val.lower() in ("true", "1", "yes")
            else:
                config[key] = env_val
    
    # Apply manual dictionary overrides if provided
    if overrides:
        config.update(overrides)
        
    return config

if __name__ == "__main__":
    # Demonstrate loading process
    current_config = load_config({"RPC_TIMEOUT": 45})
    print(f"Loaded configuration: {current_config}")