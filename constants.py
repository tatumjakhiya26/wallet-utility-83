import os

# Crypto network configuration
MAINNET_RPC = "https://mainnet.infura.io/v3/"
TESTNET_RPC = "https://sepolia.infura.io/v3/"

# Wallet constraints and defaults
DEFAULT_GAS_LIMIT = 21000
MIN_CONFIRMATIONS = 3
MAX_RETRIES = 5

# Environment keys
WALLET_PRIVATE_KEY_ENV = "WALLET_PRIVATE_KEY"
API_KEY_ENV = "RPC_API_KEY"

# Supported tokens
SUPPORTED_TOKENS = {
    "ETH": "0x0000000000000000000000000000000000000000",
    "USDC": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "USDT": "0xdAC17F958D2ee523a2206206994597C13D831ec7"
}

# Validation patterns
ADDRESS_PATTERN = r"^0x[a-fA-F0-9]{40}$"

# Timeouts in seconds
REQUEST_TIMEOUT = 30
POLLING_INTERVAL = 15