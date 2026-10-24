"""Crypto data normalization and formatting handler for wallet payloads."""

from typing import Dict, Any, Union


def wei_to_ether(wei_value: Union[int, str]) -> float:
    """Convert Wei (int or hex string) to Ether float value."""
    if isinstance(wei_value, str):
        if wei_value.startswith("0x"):
            wei_value = int(wei_value, 16)
        else:
            wei_value = int(wei_value)
    return wei_value / 10**18


def satoshi_to_btc(satoshi_value: Union[int, str]) -> float:
    """Convert Satoshi value to BTC float value."""
    return int(satoshi_value) / 10**8


def normalize_transaction(tx_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract and format key transaction details from raw wallet API responses.
    Handles both EVM hex values and standard integer amounts.
    """
    tx_hash = tx_data.get("hash") or tx_data.get("txid", "")
    sender = tx_data.get("from") or tx_data.get("sender", "")
    recipient = tx_data.get("to") or tx_data.get("recipient", "")
    raw_value = tx_data.get("value", 0)

    if isinstance(raw_value, str) and raw_value.startswith("0x"):
        amount_wei = int(raw_value, 16)
    else:
        amount_wei = int(raw_value)

    amount_eth = wei_to_ether(amount_wei)
    confirmations = tx_data.get("confirmations", 0)

    return {
        "tx_hash": str(tx_hash).lower(),
        "sender": str(sender).lower(),
        "recipient": str(recipient).lower(),
        "amount_wei": amount_wei,
        "amount_eth": round(amount_eth, 6),
        "block_number": tx_data.get("blockNumber") or tx_data.get("block_height"),
        "status": "confirmed" if confirmations > 0 else "pending",
    }
