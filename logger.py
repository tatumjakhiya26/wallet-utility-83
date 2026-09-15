import logging
import sys
from typing import Optional

class WalletLogger:
    def __init__(self, name: str = 'wallet-utility-83'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def safe_log_error(self, message: str, context: Optional[dict] = None) -> None:
        try:
            log_payload = {'error': message, 'meta': context or {}}
            self.logger.error(f'Critical failure: {log_payload}')
        except Exception as e:
            # fallback for serialization failures
            sys.stderr.write(f'Logging failure: {str(e)}\n')

    def log_tx_attempt(self, tx_id: str, status: str) -> None:
        try:
            if not tx_id:
                raise ValueError('Transaction ID missing')
            self.logger.info(f'Transaction {tx_id} status updated to {status}')
        except (ValueError, TypeError) as e:
            self.safe_log_error('Invalid transaction metadata', {'error': str(e)})
        except Exception:
            self.safe_log_error('Unexpected logging error')