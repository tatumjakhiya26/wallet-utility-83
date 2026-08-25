import os
from typing import Dict, List

# Supported cryptocurrencies
SUPPORTED_COINS: List[str] = ["BTC", "ETH", "SOL", "LTC", "XRP"]

# Blockchain API endpoints
BLOCKCHAIN_APIS: Dict[str, str] = {
    "BTC": "https://api.blockcypher.com/v1/btc/main",
    "ETH": "https://api.etherscan.io/api",
    "SOL": "https://api.mainnet-beta.solana.com",
    "LTC": "https://api.blockcypher.com/v1/ltc/main",
    "XRP": "https://data.ripple.com/v2"
}

# Default settings
DEFAULT_GAS_LIMIT: int = 21000
DEFAULT_CONFIRMATIONS: int = 6
MAX_TRANSACTION_AMOUNT: float = 1000000.0

# Wallet storage paths
WALLET_DATA_DIR: str = os.path.join(os.path.expanduser("~"), ".wallet-utility-83")
WALLET_FILE: str = "wallet.dat"
LOG_FILE: str = "wallet.log"

# Network identifiers
MAINNET: str = "mainnet"
TESTNET: str = "testnet"

# Error codes and messages
ERROR_CODES: Dict[str, int] = {
    "INVALID_ADDRESS": 1001,
    "INSUFFICIENT_FUNDS": 1002,
    "NETWORK_ERROR": 1003,
    "INVALID_KEY": 1004
}

ERROR_MESSAGES: Dict[int, str] = {
    1001: "Invalid wallet address",
    1002: "Insufficient balance",
    1003: "Network connection failed",
    1004: "Invalid private key"
}

# Rate limits
MAX_REQUESTS_PER_MINUTE: int = 60
REQUEST_TIMEOUT: int = 30

def get_api_endpoint(coin: str, network: str = MAINNET) -> str:
    """Get the appropriate API endpoint for the coin and network."""
    if coin not in SUPPORTED_COINS:
        raise ValueError("Unsupported coin: " + coin)
    base = BLOCKCHAIN_APIS.get(coin, "")
    if network == TESTNET:
        if coin in ["BTC", "LTC"]:
            base = base.replace("/main", "/test")
        elif coin == "ETH":
            base = "https://api-ropsten.etherscan.io/api"
    return base

def is_coin_supported(coin: str) -> bool:
    """Check if coin is supported."""
    return coin.upper() in SUPPORTED_COINS

def get_error_message(code: int) -> str:
    """Retrieve error message by code."""
    return ERROR_MESSAGES.get(code, "Unknown error")

if __name__ == "__main__":
    print("Supported coins:", SUPPORTED_COINS)
    print("BTC endpoint:", get_api_endpoint("BTC"))
    print("Supported ETH:", is_coin_supported("eth"))
    print("Error 1002:", get_error_message(1002))