import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG_PATH = Path.home() / ".wallet_utility" / "config.json"

DEFAULT_SETTINGS: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "gas_limit_multiplier": 1.1,
    "request_timeout": 30,
    "auto_approve": False,
    "max_fee_per_gas_gwei": 50.0,
    "log_level": "INFO",
}


@dataclass
class WalletConfig:
    network: str
    rpc_url: str
    gas_limit_multiplier: float
    request_timeout: int
    auto_approve: bool
    max_fee_per_gas_gwei: float
    log_level: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def load_config(config_path: Optional[Path] = None) -> WalletConfig:
    """Load configuration from JSON, using default values as fallback."""
    target_path = config_path or DEFAULT_CONFIG_PATH
    merged_settings = DEFAULT_SETTINGS.copy()

    if target_path.exists():
        try:
            with open(target_path, "r", encoding="utf-8") as f:
                user_settings = json.load(f)
                if isinstance(user_settings, dict):
                    merged_settings.update(user_settings)
        except (json.JSONDecodeError, OSError) as err:
            print(f"Warning: Failed to load config file: {err}")

    # Apply environment variable overrides if present
    if env_rpc := os.getenv("WALLET_RPC_URL"):
        merged_settings["rpc_url"] = env_rpc
    if env_net := os.getenv("WALLET_NETWORK"):
        merged_settings["network"] = env_net

    return WalletConfig(**merged_settings)
