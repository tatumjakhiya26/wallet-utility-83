import os

# Base directory for the wallet utility
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# API URLs
API_URL = "https://api.crypto-wallet.com"

# Default settings
DEFAULT_CURRENCY = "USD"
DEFAULT_TRANSACTION_FEE = 0.01

# Supported cryptocurrencies
SUPPORTED_CURRENCIES = [
    "BTC",
    "ETH",
    "LTC",
    "XRP",
    "BCH",
]

# Transaction status
TRANSACTION_STATUS = {
    "PENDING": "Pending",
    "COMPLETED": "Completed",
    "FAILED": "Failed",
}

# Maximum transaction limits
MAX_TRANSACTION_LIMIT = 10000
MIN_TRANSACTION_LIMIT = 1

# Configurations for logging
LOG_LEVEL = "INFO"
LOG_FILE_PATH = os.path.join(BASE_DIR, 'wallet.log')

# Error codes
ERROR_CODES = {
    100: "Insufficient funds",
    101: "Invalid currency",
    102: "Network error",
}