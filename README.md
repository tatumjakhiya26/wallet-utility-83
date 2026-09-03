[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# wallet-utility-83

`wallet-utility-83` is an asynchronous Python toolkit designed for high-throughput crypto wallet address validation and multi-chain balance monitoring. It provides developers with a unified interface to interact with EVM and Solana RPC nodes without relying on bulky external framework dependencies.

## Features

* **Multi-Chain Address Validation:** Validates formatting, checksums, and network routing for EVM (ERC-20) and Solana (SPL) public keys.
* **Concurrent RPC Querying:** Asynchronously fetches native token and contract balances across multiple network endpoints using `aiohttp`.
* **Keypair Management:** Generates BIP-39 compliant seed phrases and creates password-encrypted JSON keyfiles locally.
* **Fee Market Estimation:** Calculates real-time gas prices and priority fees to help schedule cost-efficient transactions.

## Installation

Install the package directly via `pip`:

```bash
pip install wallet-utility-83
```

Alternatively, build from source:

```bash
git clone https://github.com/Developer/wallet-utility-83.git
cd wallet-utility-83
pip install -r requirements.txt
```

## Quick Start

```python
import asyncio
from wallet_utility_83 import MultiChainClient

async def main():
    client = MultiChainClient(
        evm_rpc="https://eth.llamarpc.com",
        solana_rpc="https://api.mainnet-beta.solana.com"
    )

    # Check EVM address and fetch native balance
    eth_address = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    if client.is_valid_evm_address(eth_address):
        eth_balance = await client.get_eth_balance(eth_address)
        print(f"EVM Address: {eth_address}")
        print(f"ETH Balance: {eth_balance:.4f} ETH")

    # Fetch gas estimate
    gas_price = await client.get_recommended_gas_price()
    print(f"