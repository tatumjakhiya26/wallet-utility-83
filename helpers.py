from typing import Union, Optional
import hashlib

def validate_address(address: str) -> bool:
    """
    Checks if a crypto wallet address is valid format.
    
    :param address: The address string to validate
    :return: Boolean indicating validity
    """
    return len(address) in [26, 34, 42] and address.isalnum()

def format_amount(amount: Union[int, float]) -> str:
    """
    Converts numeric amounts to string for logging.
    
    :param amount: Numeric crypto value
    :return: Formatted string representation
    """
    return f"{float(amount):.8f}"

def generate_tx_hash(payload: str) -> str:
    """
    Creates a SHA-256 hash for transaction tracking.
    
    :param payload: Data string to hash
    :return: Hexadecimal hash string
    """
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()

def normalize_network(chain_id: Optional[int]) -> str:
    """
    Maps internal chain identifiers to network names.
    
    :param chain_id: Integer network identifier
    :return: Name of the blockchain network
    """
    mapping = {1: "mainnet", 5: "goerli", 137: "polygon"}
    return mapping.get(chain_id, "unknown")