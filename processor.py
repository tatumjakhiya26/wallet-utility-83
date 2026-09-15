import concurrent.futures
import hashlib
from typing import List, Dict, Any, Tuple

class TransactionProcessor:
    '''
    Optimized processor for handling bulk crypto transaction validations
    and hashing using thread pools and efficient memory structures.
    '''
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    @staticmethod
    def compute_tx_hash(tx_data: bytes) -> str:
        '''
        Computes double SHA-256 hash for a raw transaction payload.
        '''
        first_sha = hashlib.sha256(tx_data).digest()
        second_sha = hashlib.sha256(first_sha).digest()
        return second_sha.hex()

    def process_batch(self, transactions: List[bytes]) -> List[str]:
        '''
        Parallelizes the hashing of bulk raw transactions to utilize multi-core CPUs.
        '''
        if not transactions:
            return []

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(self.compute_tx_hash, transactions))
        return results

    def validate_and_hash_batch(self, payloads: List[Dict[str, Any]]) -> Tuple[List[str], List[int]]:
        '''
        Validates payload structure and computes tx hashes in parallel.
        Returns a tuple of successful hashes and indices of failed payloads.
        '''
        valid_payloads = []
        failed_indices = []
        
        for index, payload in enumerate(payloads):
            raw_tx = payload.get('raw_tx')
            if isinstance(raw_tx, bytes) and len(raw_tx) > 0:
                valid_payloads.append((index, raw_tx))
            else:
                failed_indices.append(index)

        if not valid_payloads:
            return [], failed_indices

        raw_bytes_list = [item[1] for item in valid_payloads]
        hashes = self.process_batch(raw_bytes_list)

        final_hashes = [None] * len(payloads)
        for (original_index, _), tx_hash in zip(valid_payloads, hashes):
            final_hashes[original_index] = tx_hash

        clean_hashes = [h for h in final_hashes if h is not None]
        return clean_hashes, failed_indices