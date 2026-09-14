# wallet-utility-83

`wallet-utility-83` is a lightweight Python toolkit designed for automated wallet address generation, balance monitoring, and transaction parsing. It streamlines interaction with EVM-compatible chains by abstracting complex RPC calls into simple, reusable functions.

### Features
*   **Hierarchical Deterministic (HD) Wallet Generation:** Effortlessly derive multiple unique addresses and private keys using BIP-39 mnemonic seeds.
*   **Real-time Balance Aggregation:** Query balances across multiple addresses simultaneously with integrated asynchronous HTTP requests to minimize latency.
*   **Transaction Decoder:** Parse raw hexadecimal transaction data into human-readable JSON formats to verify contract interactions before signing.
*   **Batch Export:** Securely export address-private key pairs into encrypted CSV files for archival or cold storage migration.

### Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/wallet-utility-83.git
cd wallet-utility-83
pip install -r requirements.txt
```

### Usage

To generate a new mnemonic and derive the first five associated addresses, run the following:

```python
from utils import wallet_manager

# Generate a new master seed
mnemonic = wallet_manager.generate_mnemonic()
print(f"Seed Phrase: {mnemonic}")

# Derive addresses
wallets = wallet_manager.derive_wallets(mnemonic, count=5)
for wallet in wallets:
    print(f"Address: {wallet['address']} | Key: {wallet['private_key']}")
```

To check balances for a list of addresses on the Ethereum mainnet:

```python
addresses = ["0x...", "0x..."]
balances = wallet_manager.get_batch_balances(addresses, provider_url="https://eth.llamarpc.com")
print(balances)
```

### License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.