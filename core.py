import re
from typing import List

HARDENED_OFFSET = 0x80000000

def parse_derivation_path(path: str) -> List[int]:
    """
    Parses a BIP32 derivation path string into a list of integer indices.
    Supports standard wallet formats like "m/44'/60'/0'/0/0" or "m/44H/60H/0H/0/0".
    """
    if not isinstance(path, str):
        raise TypeError("Derivation path must be a string")

    path = path.strip()
    if not path.startswith("m"):
        raise ValueError("Derivation path must start with 'm'")

    parts = path.split("/")[1:]
    if not parts:
        return []

    indices = []
    for part in parts:
        if not part:
            raise ValueError("Empty segment in derivation path")

        is_hardened = False
        if part.endswith("'") or part.lower().endswith("h"):
            is_hardened = True
            part = part[:-1]

        if not part.isdigit():
            raise ValueError(f"Invalid path component: {part}")

        index = int(part)
        if index >= HARDENED_OFFSET:
            raise ValueError(f"Index {index} exceeds maximum allowable BIP32 limit")

        if is_hardened:
            index += HARDENED_OFFSET

        indices.append(index)

    return indices
