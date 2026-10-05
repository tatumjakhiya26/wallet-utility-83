import re
from typing import Tuple

ETH_ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
BTC_ADDRESS_PATTERN = re.compile(r'^(1|3|bc1q)[a-zA-HJ-NP-Z0-9]{25,59}$')


def validate_ethereum_address(address: str) -> bool:
    '''Validate if the given string is a correctly formatted Ethereum address.

    Args:
        address (str): The Ethereum address to validate.

    Returns:
        bool: True if the address format is valid, False otherwise.
    '''
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_PATTERN.match(address))


def validate_bitcoin_address(address: str) -> bool:
    '''Validate if the given string is a likely valid Bitcoin address.

    Supports Legacy (1...), Pay-to-Script-Hash (3...), and Bech32 (bc1...).

    Args:
        address (str): The Bitcoin address to validate.

    Returns:
        bool: True if the address format is valid, False otherwise.
    '''
    if not isinstance(address, str):
        return False
    return bool(BTC_ADDRESS_PATTERN.match(address))


def validate_mnemonic(mnemonic: str, expected_words: Tuple[int, ...] = (12, 15, 18, 21, 24)) -> bool:
    '''Validate a BIP-39 mnemonic seed phrase format and word count.

    Args:
        mnemonic (str): The space-separated mnemonic phrase.
        expected_words (Tuple[int, ...]): Allowed word counts. Defaults to BIP-39 sizes.

    Returns:
        bool: True if the phrase format is valid, False otherwise.
    '''
    if not isinstance(mnemonic, str):
        return False

    words = mnemonic.strip().split()
    if len(words) not in expected_words:
        return False

    return all(word.isalpha() for word in words)
