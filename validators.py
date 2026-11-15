import re


def is_valid_eth_address(address: str) -> bool:
    """Check if string is a valid Ethereum hex address."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def is_valid_btc_address(address: str) -> bool:
    """Check if string is a valid Bitcoin address (Legacy, P2SH, or SegWit)."""
    if not isinstance(address, str):
        return False
    legacy_pattern = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    segwit_pattern = r"^bc1[a-0-9]{39,59}$"
    return bool(re.match(legacy_pattern, address) or re.match(segwit_pattern, address))


def is_valid_sol_address(address: str) -> bool:
    """Check if string is a valid Base58 Solana public key address."""
    if not isinstance(address, str):
        return False
    sol_pattern = r"^[1-9A-HJ-NP-Za-km-z]{32,44}$"
    return bool(re.match(sol_pattern, address))


def validate_wallet_address(address: str, chain: str) -> bool:
    """
    Validate a wallet address for a specified crypto chain.
    
    Supported chains: 'eth', 'btc', 'sol'
    """
    chain_map = {
        "eth": is_valid_eth_address,
        "ethereum": is_valid_eth_address,
        "btc": is_valid_btc_address,
        "bitcoin": is_valid_btc_address,
        "sol": is_valid_sol_address,
        "solana": is_valid_sol_address,
    }
    
    validator = chain_map.get(chain.lower().strip())
    if not validator:
        raise ValueError(f"Unsupported blockchain network: {chain}")
    
    return validator(address)
