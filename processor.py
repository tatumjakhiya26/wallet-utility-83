from dataclasses import dataclass, field
from typing import List, Dict
import re


@dataclass
class WalletEntry:
    address: str
    chain: str
    balance: float = 0.0
    is_active: bool = True
    tags: List[str] = field(default_factory=list)


class WalletDataProcessor:
    """Processor for cleaning and reorganizing crypto wallet records."""

    ETH_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
    BTC_ADDRESS_REGEX = re.compile(r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,62}$")

    def __init__(self, raw_entries: List[Dict]):
        self.raw_entries = raw_entries

    def sanitize_address(self, address: str) -> str:
        """Strip whitespace and normalize EVM hex addresses to lowercase."""
        clean = address.strip()
        if clean.startswith("0x"):
            return clean.lower()
        return clean

    def validate_and_parse(self) -> List[WalletEntry]:
        """Validate raw dictionary items into structured WalletEntry objects."""
        processed = []
        for item in self.raw_entries:
            raw_addr = item.get("address", "")
            clean_addr = self.sanitize_address(raw_addr)
            chain = item.get("chain", "ethereum").lower()

            if chain == "ethereum" and not self.ETH_ADDRESS_REGEX.match(clean_addr):
                continue
            if chain == "bitcoin" and not self.BTC_ADDRESS_REGEX.match(clean_addr):
                continue

            entry = WalletEntry(
                address=clean_addr,
                chain=chain,
                balance=float(item.get("balance", 0.0)),
                is_active=bool(item.get("is_active", True)),
                tags=[t.strip().lower() for t in item.get("tags", [])]
            )
            processed.append(entry)
        return processed

    def reorganize_by_chain(self, entries: List[WalletEntry]) -> Dict[str, List[WalletEntry]]:
        """Group processed entries by blockchain network sorted by balance."""
        grouped: Dict[str, List[WalletEntry]] = {}
        for entry in entries:
            grouped.setdefault(entry.chain, []).append(entry)

        for chain in grouped:
            grouped[chain].sort(key=lambda x: x.balance, reverse=True)

        return grouped
