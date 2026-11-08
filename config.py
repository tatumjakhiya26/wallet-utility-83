import os
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class NetworkConfig:
    chain_id: int
    rpc_url: str
    symbol: str
    explorer_url: str
    default_gas_limit: int = 21000


DEFAULT_NETWORKS: Dict[str, NetworkConfig] = {
    "mainnet": NetworkConfig(
        chain_id=1,
        rpc_url=os.getenv("ETH_MAINNET_RPC", "https://eth.llamarpc.com"),
        symbol="ETH",
        explorer_url="https://etherscan.io",
    ),
    "polygon": NetworkConfig(
        chain_id=137,
        rpc_url=os.getenv("POLYGON_RPC", "https://polygon-rpc.com"),
        symbol="POL",
        explorer_url="https://polygonscan.com",
        default_gas_limit=30000,
    ),
    "arbitrum": NetworkConfig(
        chain_id=42161,
        rpc_url=os.getenv("ARBITRUM_RPC", "https://arb1.arbitrum.io/rpc"),
        symbol="ETH",
        explorer_url="https://arbiscan.io",
    ),
}


class WalletConfigManager:
    """Manages runtime configuration and network parameters for wallet operations."""

    def __init__(self, storage_dir: Optional[str] = None):
        base_dir = storage_dir or os.getenv("WALLET_STORAGE_DIR", "~/.wallet-utility")
        self.storage_dir = os.path.expanduser(base_dir)
        self.networks: Dict[str, NetworkConfig] = DEFAULT_NETWORKS.copy()
        self._ensure_storage_directory()

    def _ensure_storage_directory(self) -> None:
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir, mode=0o700, exist_ok=True)

    def get_network(self, name: str) -> NetworkConfig:
        network = self.networks.get(name.lower())
        if not network:
            raise KeyError(f"Unsupported network '{name}' requested")
        return network

    def register_custom_network(self, name: str, config: NetworkConfig) -> None:
        self.networks[name.lower()] = config
