# wallet-utility-83

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`wallet-utility-83` is a lightweight Python toolkit designed for non-custodial EVM wallet management and multi-chain balance aggregation. It simplifies HD wallet derivation, automated token tracking, and local transaction signing without relying on third-party backend servers.

## Features

* **BIP-44 HD Wallet Derivation:** Deterministically generate EVM-compatible addresses and private keys from standard 12 or 24-word seed phrases.
* **Multi-Chain ERC-20 Tracking:** Query Native (ETH, MATIC, BNB) and custom ERC-20 token balances across multiple RPC endpoints concurrently.
* **Offline Transaction Builder:** Form, sign, and serialize EVM transactions locally using raw private keys for enhanced operational security.
* **Gas Estimation Engine:** Calculate dynamic EIP-1559 gas fees based on real-time network block header analysis.

## Installation

Install the package directly from source:

```bash
git clone https://github.com/Developer/wallet-utility-83.git
cd wallet-utility-83
pip install -r requirements.txt
```

## Quick Start

The following example demonstrates how to derive an address from a mnemonic and check its native ETH balance.

```python
from wallet_utility import WalletManager

# Initialize manager with an Ethereum RPC endpoint
wm = WalletManager(rpc_url="https://cloudflare-eth.com")

# Derive account at index 0 from a standard mnemonic
mnemonic = "test test test test test test test test test test test junk"
account = wm.from_mnemonic(mnemonic, account_index=0)

print(f"Derived Address: {account.address}")

# Fetch real-time balance
balance = wm.get_native_balance(account.address)
print(f"ETH Balance: {balance:.4f} ETH")
```

## License

Distributed under the MIT License. See `LICENSE` for more information.