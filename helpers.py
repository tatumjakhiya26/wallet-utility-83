import logging
from typing import Optional

def validate_address(address: str) -> bool:
    """verify crypto wallet address format"""
    if not address or len(address) < 26 or len(address) > 35:
        return False
    return address.isalnum()

def format_balance(amount: float, decimals: int = 8) -> str:
    """format float balance to precise string"""
    return f"{amount:.{decimals}f}"

def mask_key(key: str) -> str:
    """obfuscate private key for logs"""
    if len(key) < 8:
        return "********"
    return f"{key[:4]}...{key[-4:]}"

class WalletError(Exception):
    """base exception for wallet operations"""
    pass

def get_logger(name: str) -> logging.Logger:
    """standardized logger configuration"""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger