import re

class WalletProcessor:
    """Handles validation and processing for crypto transactions."""
    
    def __init__(self):
        self.address_pattern = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

    def validate_input(self, address: str, amount: float) -> bool:
        """Check if address and amount meet security criteria."""
        if not isinstance(address, str) or not self.address_pattern.match(address):
            return False
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False
        return True

    def run_main_loop(self, queue: list):
        """Process transaction queue with input validation."""
        for entry in queue:
            addr = entry.get('address')
            amt = entry.get('amount')

            if not self.validate_input(addr, amt):
                print(f"Validation failed for entry: {entry}")
                continue

            try:
                self._execute_transfer(addr, amt)
            except Exception as e:
                print(f"Transaction error: {e}")

    def _execute_transfer(self, address: str, amount: float):
        """Mock logic for blockchain transfer."""
        print(f"Transferring {amount} to {address}...")

if __name__ == '__main__':
    processor = WalletProcessor()
    transactions = [
        {'address': '0x1234567890123456789012345678901234567890', 'amount': 1.5},
        {'address': 'invalid-addr', 'amount': 10},
        {'address': '0xABC1234567890123456789012345678901234567', 'amount': -5}
    ]
    processor.run_main_loop(transactions)