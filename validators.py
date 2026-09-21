import re

# Regex patterns for common cryptocurrency address formats
ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
BTC_LEGACY_PATTERN = re.compile(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$")
BTC_BECH32_PATTERN = re.compile(r"^bc1[a-0-z1-9]{8,87}$")
SOL_ADDRESS_PATTERN = re.compile(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$")


def is_valid_eth_address(address: str) -> bool:
    """Validate Ethereum address format (hexadecimal string starting with 0x)."""
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_PATTERN.match(address))


def is_valid_btc_address(address: str) -> bool:
    """Validate Bitcoin address format (Legacy, Script, or Native SegWit)."""
    if not isinstance(address, str):
        return False
    return bool(
        BTC_LEGACY_PATTERN.match(address) or BTC_BECH32_PATTERN.match(address)
    )


def is_valid_solana_address(address: str) -> bool:
    """Validate Solana address format (Base58 encoded key)."""
    if not isinstance(address, str):
        return False
    return bool(SOL_ADDRESS_PATTERN.match(address))


def validate_address(address: str, chain: str) -> bool:
    """Validate cryptocurrency wallet address for a specific blockchain network.

    Args:
        address: The wallet address string to validate.
        chain: The blockchain network identifier ('eth', 'btc', 'sol').

    Returns:
        True if valid for the specified chain, False otherwise.
    """
    chain_key = chain.strip().lower()
    validators = {
        "eth": is_valid_eth_address,
        "ethereum": is_valid_eth_address,
        "btc": is_valid_btc_address,
        "bitcoin": is_valid_btc_address,
        "sol": is_valid_solana_address,
        "solana": is_valid_solana_address,
    }

    validator_fn = validators.get(chain_key)
    if not validator_fn:
        raise ValueError(f"Unsupported blockchain network: {chain}")

    return validator_fn(address)
