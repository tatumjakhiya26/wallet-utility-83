# wallet-utility-83

A high-performance Python toolkit for managing hierarchical deterministic (HD) crypto wallets and performing secure blockchain transactions. This utility streamlines complex wallet management tasks, ensuring reliable signing and key derivation for multi-chain environments.

## Features

*   **BIP-39 Implementation:** Generate secure mnemonic phrases and derive deterministic addresses using standard derivation paths.
*   **Multi-Chain Support:** Native integration for EVM-based networks with robust transaction signing and raw payload broadcasting.
*   **Balance Aggregation:** Efficiently query and parse wallet balances across multiple addresses through RPC interfaces.
*   **Encrypted Storage:** Built-in AES-256 encryption to secure private keys at rest within your local file system.

## Installation

Ensure you have Python 3.9+ installed. It is recommended to use a virtual environment:

```bash
# Clone the repository
git clone https://github.com/Developer/wallet-utility-83.git
cd wallet-utility-83

# Install dependencies
pip install -r requirements.txt
```

## Basic Usage

To generate a new wallet and view its details, run the following command:

```python
from wallet_utility import WalletManager

# Initialize manager and generate a new BIP-39 wallet
manager = WalletManager()
wallet = manager.create_new_wallet(passphrase="secure_optional_password")

print(f"Address: {wallet.address}")
print(f"Mnemonic: {wallet.mnemonic}")
```

To sign a transaction manually:

```python
tx = {
    'to': '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
    'value': 1000000000000000000,
    'gas': 21000,
    'nonce': 0
}

signed_tx = manager.sign_transaction(tx, private_key=wallet.private_key)
print(f"Signed Raw Hex: {signed_tx.hex()}")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.