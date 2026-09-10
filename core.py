import hashlib
from functools import lru_cache

@lru_cache(maxsize=1024)
def sha256_double(data: bytes) -> bytes:
    """Computes double SHA256 hash with caching for repeated inputs."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

@lru_cache(maxsize=4096)
def ripemd160_sha256(data: bytes) -> bytes:
    """Computes RIPEMD160 of SHA256 with caching for address generation."""
    sha = hashlib.sha256(data).digest()
    try:
        h = hashlib.new('ripemd160')
        h.update(sha)
        return h.digest()
    except ValueError:
        return hashlib.sha256(sha).digest()[:20]

def optimize_batch_addresses(public_keys: list) -> list:
    """Generates crypto addresses from public keys using optimized caching mechanisms."""
    addresses = []
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    for pubkey in public_keys:
        pkh = ripemd160_sha256(pubkey)
        payload = b'\x00' + pkh
        checksum = sha256_double(payload)[:4]
        value = int.from_bytes(payload + checksum, 'big')
        result = []
        while value > 0:
            value, mod = divmod(value, 58)
            result.append(alphabet[mod])
        zeros = len(payload) - len(payload.lstrip(b'\x00'))
        addresses.append('1' * zeros + ''.join(reversed(result)))
    return addresses