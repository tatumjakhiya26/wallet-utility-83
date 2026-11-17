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
    """Loads configuration from a JSON file with defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load {config_path}: {e}. Using defaults.")
    
    return config

def get_rpc_url() -> str:
    """Helper to retrieve RPC endpoint."""
    return load_config().get("rpc_url", DEFAULT_CONFIG["rpc_url"])

if __name__ == "__main__":
    # Example usage for wallet-utility-83
    settings = load_config()
    print(f"Active config: {settings}")