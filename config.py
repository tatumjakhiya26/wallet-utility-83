import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

DEFAULT_SETTINGS: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.public.blastapi.io",
    "gas_limit_multiplier": 1.15,
    "request_timeout_seconds": 30,
    "max_retries": 3,
    "enable_mempool_monitoring": False,
}


@dataclass
class WalletConfig:
    network: str = DEFAULT_SETTINGS["network"]
    rpc_url: str = DEFAULT_SETTINGS["rpc_url"]
    gas_limit_multiplier: float = DEFAULT_SETTINGS["gas_limit_multiplier"]
    request_timeout_seconds: int = DEFAULT_SETTINGS["request_timeout_seconds"]
    max_retries: int = DEFAULT_SETTINGS["max_retries"]
    enable_mempool_monitoring: bool = DEFAULT_SETTINGS["enable_mempool_monitoring"]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WalletConfig":
        valid_keys = cls.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered_data)


def load_config(filepath: Path = Path("wallet_config.json")) -> WalletConfig:
    """Loads wallet configuration from JSON and environment overrides with defaults."""
    config_data = DEFAULT_SETTINGS.copy()

    if filepath.exists():
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                file_data = json.load(f)
                config_data.update(file_data)
        except (json.JSONDecodeError, OSError):
            pass

    env_mappings = {
        "WALLET_NETWORK": ("network", str),
        "WALLET_RPC_URL": ("rpc_url", str),
        "WALLET_GAS_MULTIPLIER": ("gas_limit_multiplier", float),
        "WALLET_TIMEOUT": ("request_timeout_seconds", int),
        "WALLET_MAX_RETRIES": ("max_retries", int),
    }

    for env_var, (config_key, type_caster) in env_mappings.items():
        val = os.getenv(env_var)
        if val is not None:
            try:
                config_data[config_key] = type_caster(val)
            except ValueError:
                pass

    return WalletConfig.from_dict(config_data)
