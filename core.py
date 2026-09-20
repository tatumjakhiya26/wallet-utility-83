import hashlib
import functools
from typing import List, Dict


@functools.lru_cache(maxsize=2048)
def fast_sha256(data: bytes) -> bytes:
    """Compute SHA-256 hash with memory caching for frequent payloads."""
    return hashlib.sha256(data).digest()


@functools.lru_cache(maxsize=2048)
def ripemd160_sha256(data: bytes) -> bytes:
    """Compute optimized HASH160 (RIPEMD-160 of SHA-256) for public keys."""
    sha_hash = fast_sha256(data)
    h = hashlib.new('ripemd160')
    h.update(sha_hash)
    return h.digest()


class BatchAddressProcessor:
    """High-performance wallet address derivation and memoized batch processor."""

    def __init__(self, cache_limit: int = 4096):
        self._address_cache: Dict[bytes, str] = {}
        self.cache_limit = cache_limit

    def process_pubkeys_batch(self, pubkeys: List[bytes]) -> List[str]:
        """Batch convert raw public keys into address hashes with caching."""
        results: List[str] = []
        for pubkey in pubkeys:
            cached_addr = self._address_cache.get(pubkey)
            if cached_addr is not None:
                results.append(cached_addr)
                continue

            addr_hash = ripemd160_sha256(pubkey).hex()
            if len(self._address_cache) < self.cache_limit:
                self._address_cache[pubkey] = addr_hash

            results.append(addr_hash)
        return results

    def clear_cache(self) -> None:
        """Flush processor memory caches."""
        self._address_cache.clear()
        fast_sha256.cache_clear()
        ripemd160_sha256.cache_clear()
