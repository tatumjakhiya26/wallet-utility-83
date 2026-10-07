import os
from typing import Any, Dict

# Default configuration settings for wallet-utility-83
DEFAULT_CONFIG = {
    "NETWORK": "mainnet",
    "RPC_ENDPOINT": "https://api.mainnet-beta.solana.com",
    "TIMEOUT_SECONDS": 30,
    "MAX_RETRIES": 3,
    "LOG_LEVEL": "INFO"
}

def load_config(env_prefix: str = "WALLET_") -> Dict[str, Any]:
    """
    Loads configuration from environment variables with defaults.
    Iterates over default keys and checks for matching env vars.
    """
    config = DEFAULT_CONFIG.copy()
    
    for key in config.keys():
        env_key = f"{env_prefix}{key}"
        value = os.environ.get(env_key)
        
        if value is not None:
            # Handle type casting for non-string defaults
            default_val = config[key]
            if isinstance(default_val, int):
                config[key] = int(value)
            else:
                config[key] = value
                
    return config

if __name__ == "__main__":
    # Example usage for wallet service
    settings = load_config()
    print(f"Loaded network: {settings['NETWORK']}")