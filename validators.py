import re
from typing import Optional

def is_valid_address(address: str, chain_type: str = "evm") -> bool:
    """
    Validate crypto wallet address format based on chain type.

    :param address: The wallet address string to check
    :param chain_type: Network type, defaults to 'evm'
    :return: Boolean indicating validity
    """
    if chain_type == "evm":
        return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))
    if chain_type == "bitcoin":
        return bool(re.match(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", address))
    return False

def validate_amount(amount: str) -> Optional[float]:
    """
    Convert string amount to float if positive.

    :param amount: Numeric string input
    :return: Float value or None if invalid
    """
    try:
        val = float(amount)
        return val if val > 0 else None
    except ValueError:
        return None

def sanitize_memo(memo: str) -> str:
    """
    Remove non-alphanumeric characters from memo fields.

    :param memo: Input transaction memo
    :return: Cleaned alphanumeric string
    """
    return re.sub(r"[^a-zA-Z0-9 ]", "", memo).strip()