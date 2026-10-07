import hashlib
from typing import Optional

def generate_address_checksum(public_key: str) -> str:
    """Generates a standard EIP-55 style checksum for a hex address."""
    address = public_key.lower().replace('0x', '')
    hash_result = hashlib.sha3_256(address.encode()).hexdigest()
    checksum_address = '0x'
    for i, char in enumerate(address):
        if int(hash_result[i], 16) >= 8:
            checksum_address += char.upper()
        else:
            checksum_address += char
    return checksum_address

def format_wei_to_eth(wei_value: int) -> float:
    """Converts raw wei integers to standard ETH float units."""
    return float(wei_value) / 10**18

def validate_transaction_hash(tx_hash: str) -> bool:
    """Validates the format of a transaction hash string."""
    if len(tx_hash) != 66:
        return False
    try:
        int(tx_hash, 16)
        return True
    except ValueError:
        return False

def get_network_name(chain_id: Optional[int]) -> str:
    """Maps integer chain IDs to readable network strings."""
    networks = {
        1: "mainnet",
        5: "goerli",
        11155111: "sepolia"
    }
    return networks.get(chain_id, "unknown")