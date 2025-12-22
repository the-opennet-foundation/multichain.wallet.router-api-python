# MultichainWalletRouterAPI

Methods:

- <code title="get /">client.<a href="./src/multichain/wallet/router_api/_client.py">get_info</a>() -> None</code>

# Health

Types:

```python
from multichain.wallet.router_api.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/multichain/wallet/router_api/resources/health.py">check</a>() -> <a href="./src/multichain/wallet/router_api/types/health_check_response.py">HealthCheckResponse</a></code>

# Wallet

Methods:

- <code title="get /wallet/chains">client.wallet.<a href="./src/multichain/wallet/router_api/resources/wallet.py">list_chains</a>() -> None</code>
- <code title="get /wallet/add-chain/{chainId}">client.wallet.<a href="./src/multichain/wallet/router_api/resources/wallet.py">retrieve_chain</a>(chain_id) -> None</code>

# Evm

Methods:

- <code title="post /evm/{chainId}/call">client.evm.<a href="./src/multichain/wallet/router_api/resources/evm/evm.py">call_contract</a>(chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm_call_contract_params.py">params</a>) -> None</code>
- <code title="get /evm/{chainId}/balance/{address}">client.evm.<a href="./src/multichain/wallet/router_api/resources/evm/evm.py">get_balance</a>(address, \*, chain_id) -> None</code>
- <code title="get /evm/{chainId}/code/{address}">client.evm.<a href="./src/multichain/wallet/router_api/resources/evm/evm.py">get_contract_code</a>(address, \*, chain_id) -> None</code>
- <code title="get /evm/{chainId}/nft/{contractAddress}/{tokenId}">client.evm.<a href="./src/multichain/wallet/router_api/resources/evm/evm.py">get_nft_metadata</a>(token_id, \*, chain_id, contract_address) -> None</code>
- <code title="get /evm/{chainId}/nfts/{address}">client.evm.<a href="./src/multichain/wallet/router_api/resources/evm/evm.py">get_nfts</a>(address, \*, chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm_get_nfts_params.py">params</a>) -> None</code>
- <code title="get /evm/{chainId}/nonce/{address}">client.evm.<a href="./src/multichain/wallet/router_api/resources/evm/evm.py">get_nonce</a>(address, \*, chain_id) -> None</code>
- <code title="get /evm/{chainId}/tokens/{address}">client.evm.<a href="./src/multichain/wallet/router_api/resources/evm/evm.py">get_tokens</a>(address, \*, chain_id) -> None</code>
- <code title="get /evm/{chainId}/transactions/{address}">client.evm.<a href="./src/multichain/wallet/router_api/resources/evm/evm.py">get_transaction_history</a>(address, \*, chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm_get_transaction_history_params.py">params</a>) -> None</code>
- <code title="post /evm/{chainId}/simulate">client.evm.<a href="./src/multichain/wallet/router_api/resources/evm/evm.py">simulate_transaction</a>(chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm_simulate_transaction_params.py">params</a>) -> None</code>

## Chains

Methods:

- <code title="get /evm/chains/{chainId}">client.evm.chains.<a href="./src/multichain/wallet/router_api/resources/evm/chains.py">retrieve</a>(chain_id) -> None</code>
- <code title="get /evm/chains">client.evm.chains.<a href="./src/multichain/wallet/router_api/resources/evm/chains.py">list</a>() -> None</code>

## Token

Methods:

- <code title="get /evm/{chainId}/token/{tokenAddress}/allowance">client.evm.token.<a href="./src/multichain/wallet/router_api/resources/evm/token.py">get_allowance</a>(token_address, \*, chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm/token_get_allowance_params.py">params</a>) -> None</code>
- <code title="get /evm/{chainId}/token/{tokenAddress}/metadata">client.evm.token.<a href="./src/multichain/wallet/router_api/resources/evm/token.py">get_metadata</a>(token_address, \*, chain_id) -> None</code>

## Contract

Methods:

- <code title="get /evm/{chainId}/contract/{contractAddress}/metadata">client.evm.contract.<a href="./src/multichain/wallet/router_api/resources/evm/contract.py">get_metadata</a>(contract_address, \*, chain_id) -> None</code>

## Tx

Methods:

- <code title="get /evm/{chainId}/tx/{txHash}">client.evm.tx.<a href="./src/multichain/wallet/router_api/resources/evm/tx.py">get_by_hash</a>(tx_hash, \*, chain_id) -> None</code>
- <code title="post /evm/{chainId}/tx/send">client.evm.tx.<a href="./src/multichain/wallet/router_api/resources/evm/tx.py">send</a>(chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm/tx_send_params.py">params</a>) -> None</code>

## Gas

Methods:

- <code title="post /evm/{chainId}/gas/estimate">client.evm.gas.<a href="./src/multichain/wallet/router_api/resources/evm/gas.py">estimate</a>(chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm/gas_estimate_params.py">params</a>) -> None</code>
- <code title="get /evm/{chainId}/gas/price">client.evm.gas.<a href="./src/multichain/wallet/router_api/resources/evm/gas.py">get_price</a>(chain_id) -> None</code>

## Block

Methods:

- <code title="get /evm/{chainId}/block/{blockNumber}">client.evm.block.<a href="./src/multichain/wallet/router_api/resources/evm/block.py">get_by_number</a>(block_number, \*, chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm/block_get_by_number_params.py">params</a>) -> None</code>
- <code title="get /evm/{chainId}/block/number">client.evm.block.<a href="./src/multichain/wallet/router_api/resources/evm/block.py">get_current_number</a>(chain_id) -> None</code>

## Prices

Methods:

- <code title="post /evm/{chainId}/prices/by-address">client.evm.prices.<a href="./src/multichain/wallet/router_api/resources/evm/prices.py">get_by_address</a>(chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm/price_get_by_address_params.py">params</a>) -> None</code>
- <code title="post /evm/prices/by-symbol">client.evm.prices.<a href="./src/multichain/wallet/router_api/resources/evm/prices.py">get_by_symbol</a>(\*\*<a href="src/multichain/wallet/router_api/types/evm/price_get_by_symbol_params.py">params</a>) -> None</code>

## Explorer

Methods:

- <code title="get /evm/{chainId}/explorer/gas">client.evm.explorer.<a href="./src/multichain/wallet/router_api/resources/evm/explorer/explorer.py">get_gas_oracle</a>(chain_id) -> None</code>
- <code title="get /evm/{chainId}/explorer/token/{address}">client.evm.explorer.<a href="./src/multichain/wallet/router_api/resources/evm/explorer/explorer.py">get_token_info</a>(address, \*, chain_id) -> None</code>
- <code title="get /evm/{chainId}/explorer/tokentx/{address}">client.evm.explorer.<a href="./src/multichain/wallet/router_api/resources/evm/explorer/explorer.py">get_tokentx</a>(address, \*, chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm/explorer_get_tokentx_params.py">params</a>) -> None</code>
- <code title="get /evm/{chainId}/explorer/txlist/{address}">client.evm.explorer.<a href="./src/multichain/wallet/router_api/resources/evm/explorer/explorer.py">get_txlist</a>(address, \*, chain_id, \*\*<a href="src/multichain/wallet/router_api/types/evm/explorer_get_txlist_params.py">params</a>) -> None</code>

### Contract

Methods:

- <code title="get /evm/{chainId}/explorer/contract/{address}/abi">client.evm.explorer.contract.<a href="./src/multichain/wallet/router_api/resources/evm/explorer/contract.py">get_abi</a>(address, \*, chain_id) -> None</code>
- <code title="get /evm/{chainId}/explorer/contract/{address}/source">client.evm.explorer.contract.<a href="./src/multichain/wallet/router_api/resources/evm/explorer/contract.py">get_source</a>(address, \*, chain_id) -> None</code>

# Solana

Methods:

- <code title="post /solana/accounts">client.solana.<a href="./src/multichain/wallet/router_api/resources/solana/solana.py">create_multiple_accounts</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana_create_multiple_accounts_params.py">params</a>) -> None</code>
- <code title="get /solana/signatures/{address}">client.solana.<a href="./src/multichain/wallet/router_api/resources/solana/solana.py">list_signatures</a>(address, \*\*<a href="src/multichain/wallet/router_api/types/solana_list_signatures_params.py">params</a>) -> None</code>
- <code title="get /solana/tokens/{owner}">client.solana.<a href="./src/multichain/wallet/router_api/resources/solana/solana.py">list_tokens</a>(owner, \*\*<a href="src/multichain/wallet/router_api/types/solana_list_tokens_params.py">params</a>) -> None</code>
- <code title="get /solana/validators">client.solana.<a href="./src/multichain/wallet/router_api/resources/solana/solana.py">list_validators</a>() -> None</code>
- <code title="get /solana/account/{address}">client.solana.<a href="./src/multichain/wallet/router_api/resources/solana/solana.py">retrieve_account_info</a>(address) -> None</code>
- <code title="get /solana/balance/{address}">client.solana.<a href="./src/multichain/wallet/router_api/resources/solana/solana.py">retrieve_balance</a>(address) -> None</code>
- <code title="get /solana/block/{slot}">client.solana.<a href="./src/multichain/wallet/router_api/resources/solana/solana.py">retrieve_block_by_slot</a>(slot) -> None</code>
- <code title="get /solana/slot">client.solana.<a href="./src/multichain/wallet/router_api/resources/solana/solana.py">retrieve_current_slot</a>() -> None</code>
- <code title="get /solana/info">client.solana.<a href="./src/multichain/wallet/router_api/resources/solana/solana.py">retrieve_info</a>() -> None</code>
- <code title="get /solana/blockhash">client.solana.<a href="./src/multichain/wallet/router_api/resources/solana/solana.py">retrieve_latest_blockhash</a>() -> None</code>

## Token

Methods:

- <code title="get /solana/token/{mint}/largest">client.solana.token.<a href="./src/multichain/wallet/router_api/resources/solana/token.py">list_largest_accounts</a>(mint) -> None</code>
- <code title="get /solana/token/{tokenAccount}/balance">client.solana.token.<a href="./src/multichain/wallet/router_api/resources/solana/token.py">retrieve_balance</a>(token_account) -> None</code>
- <code title="get /solana/token/{mint}/supply">client.solana.token.<a href="./src/multichain/wallet/router_api/resources/solana/token.py">retrieve_total_supply</a>(mint) -> None</code>

## NFT

Methods:

- <code title="get /solana/nft/{mint}/editions">client.solana.nft.<a href="./src/multichain/wallet/router_api/resources/solana/nft.py">get_editions</a>(mint, \*\*<a href="src/multichain/wallet/router_api/types/solana/nft_get_editions_params.py">params</a>) -> None</code>

## Tx

Methods:

- <code title="get /solana/tx/{signature}">client.solana.tx.<a href="./src/multichain/wallet/router_api/resources/solana/tx.py">retrieve</a>(signature) -> None</code>
- <code title="post /solana/tx/send">client.solana.tx.<a href="./src/multichain/wallet/router_api/resources/solana/tx.py">send</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/tx_send_params.py">params</a>) -> None</code>
- <code title="post /solana/tx/simulate">client.solana.tx.<a href="./src/multichain/wallet/router_api/resources/solana/tx.py">simulate</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/tx_simulate_params.py">params</a>) -> None</code>

## Fees

Methods:

- <code title="get /solana/fees/priority">client.solana.fees.<a href="./src/multichain/wallet/router_api/resources/solana/fees.py">get_priority</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/fee_get_priority_params.py">params</a>) -> None</code>
- <code title="get /solana/fees/recent">client.solana.fees.<a href="./src/multichain/wallet/router_api/resources/solana/fees.py">get_recent</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/fee_get_recent_params.py">params</a>) -> None</code>

## Stake

Methods:

- <code title="get /solana/stake/{account}/activation">client.solana.stake.<a href="./src/multichain/wallet/router_api/resources/solana/stake.py">get_activation_status</a>(account) -> None</code>

## Inflation

Methods:

- <code title="get /solana/inflation/rate">client.solana.inflation.<a href="./src/multichain/wallet/router_api/resources/solana/inflation.py">get_rate</a>() -> None</code>
- <code title="post /solana/inflation/rewards">client.solana.inflation.<a href="./src/multichain/wallet/router_api/resources/solana/inflation.py">get_rewards</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/inflation_get_rewards_params.py">params</a>) -> None</code>

## Jupiter

Methods:

- <code title="get /solana/jupiter/price">client.solana.jupiter.<a href="./src/multichain/wallet/router_api/resources/solana/jupiter.py">get_price</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/jupiter_get_price_params.py">params</a>) -> None</code>
- <code title="get /solana/jupiter/quote">client.solana.jupiter.<a href="./src/multichain/wallet/router_api/resources/solana/jupiter.py">get_quote</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/jupiter_get_quote_params.py">params</a>) -> None</code>
- <code title="get /solana/jupiter/tokens">client.solana.jupiter.<a href="./src/multichain/wallet/router_api/resources/solana/jupiter.py">get_tokens</a>() -> None</code>
- <code title="post /solana/jupiter/swap">client.solana.jupiter.<a href="./src/multichain/wallet/router_api/resources/solana/jupiter.py">swap</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/jupiter_swap_params.py">params</a>) -> None</code>

## Terminal

Methods:

- <code title="get /solana/terminal/chart/{assetId}">client.solana.terminal.<a href="./src/multichain/wallet/router_api/resources/solana/terminal.py">get_chart</a>(asset_id, \*\*<a href="src/multichain/wallet/router_api/types/solana/terminal_get_chart_params.py">params</a>) -> None</code>
- <code title="get /solana/terminal/description/{assetId}">client.solana.terminal.<a href="./src/multichain/wallet/router_api/resources/solana/terminal.py">get_description</a>(asset_id) -> None</code>
- <code title="get /solana/terminal/holders/{assetId}">client.solana.terminal.<a href="./src/multichain/wallet/router_api/resources/solana/terminal.py">get_holders</a>(asset_id) -> None</code>
- <code title="get /solana/terminal/pools">client.solana.terminal.<a href="./src/multichain/wallet/router_api/resources/solana/terminal.py">get_pools</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/terminal_get_pools_params.py">params</a>) -> None</code>
- <code title="get /solana/terminal/txs/{assetId}">client.solana.terminal.<a href="./src/multichain/wallet/router_api/resources/solana/terminal.py">get_recent_trades</a>(asset_id, \*\*<a href="src/multichain/wallet/router_api/types/solana/terminal_get_recent_trades_params.py">params</a>) -> None</code>
- <code title="get /solana/terminal/tokens">client.solana.terminal.<a href="./src/multichain/wallet/router_api/resources/solana/terminal.py">get_tokens</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/terminal_get_tokens_params.py">params</a>) -> None</code>

## Assets

Methods:

- <code title="get /solana/asset/{assetId}">client.solana.assets.<a href="./src/multichain/wallet/router_api/resources/solana/assets.py">retrieve</a>(asset_id) -> None</code>
- <code title="post /solana/assets">client.solana.assets.<a href="./src/multichain/wallet/router_api/resources/solana/assets.py">create_multiple_assets</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/asset_create_multiple_assets_params.py">params</a>) -> None</code>
- <code title="get /solana/asset/{assetId}/proof">client.solana.assets.<a href="./src/multichain/wallet/router_api/resources/solana/assets.py">get_proof</a>(asset_id) -> None</code>
- <code title="get /solana/asset/{assetId}/signatures">client.solana.assets.<a href="./src/multichain/wallet/router_api/resources/solana/assets.py">get_signatures</a>(asset_id, \*\*<a href="src/multichain/wallet/router_api/types/solana/asset_get_signatures_params.py">params</a>) -> None</code>
- <code title="get /solana/assets/authority/{authority}">client.solana.assets.<a href="./src/multichain/wallet/router_api/resources/solana/assets.py">list_assets_by_authority</a>(authority, \*\*<a href="src/multichain/wallet/router_api/types/solana/asset_list_assets_by_authority_params.py">params</a>) -> None</code>
- <code title="get /solana/assets/creator/{creator}">client.solana.assets.<a href="./src/multichain/wallet/router_api/resources/solana/assets.py">list_assets_by_creator</a>(creator, \*\*<a href="src/multichain/wallet/router_api/types/solana/asset_list_assets_by_creator_params.py">params</a>) -> None</code>
- <code title="get /solana/assets/group/{groupKey}/{groupValue}">client.solana.assets.<a href="./src/multichain/wallet/router_api/resources/solana/assets.py">list_assets_by_group</a>(group_value, \*, group_key, \*\*<a href="src/multichain/wallet/router_api/types/solana/asset_list_assets_by_group_params.py">params</a>) -> None</code>
- <code title="get /solana/assets/{owner}">client.solana.assets.<a href="./src/multichain/wallet/router_api/resources/solana/assets.py">list_owned_assets</a>(owner, \*\*<a href="src/multichain/wallet/router_api/types/solana/asset_list_owned_assets_params.py">params</a>) -> None</code>
- <code title="post /solana/assets/search">client.solana.assets.<a href="./src/multichain/wallet/router_api/resources/solana/assets.py">search_assets</a>(\*\*<a href="src/multichain/wallet/router_api/types/solana/asset_search_assets_params.py">params</a>) -> None</code>

# Bitcoin

Methods:

- <code title="get /bitcoin/difficulty">client.bitcoin.<a href="./src/multichain/wallet/router_api/resources/bitcoin/bitcoin.py">get_difficulty</a>() -> None</code>
- <code title="get /bitcoin/hashrate">client.bitcoin.<a href="./src/multichain/wallet/router_api/resources/bitcoin/bitcoin.py">get_hashrate</a>(\*\*<a href="src/multichain/wallet/router_api/types/bitcoin_get_hashrate_params.py">params</a>) -> None</code>
- <code title="get /bitcoin/info">client.bitcoin.<a href="./src/multichain/wallet/router_api/resources/bitcoin/bitcoin.py">get_info</a>() -> None</code>
- <code title="get /bitcoin/price">client.bitcoin.<a href="./src/multichain/wallet/router_api/resources/bitcoin/bitcoin.py">get_price</a>() -> None</code>
- <code title="get /bitcoin/utxo/{txid}/{vout}">client.bitcoin.<a href="./src/multichain/wallet/router_api/resources/bitcoin/bitcoin.py">get_utxo</a>(vout, \*, txid, \*\*<a href="src/multichain/wallet/router_api/types/bitcoin_get_utxo_params.py">params</a>) -> None</code>
- <code title="get /bitcoin/validate/{address}">client.bitcoin.<a href="./src/multichain/wallet/router_api/resources/bitcoin/bitcoin.py">validate_address</a>(address) -> None</code>

## Address

Methods:

- <code title="get /bitcoin/address/{address}">client.bitcoin.address.<a href="./src/multichain/wallet/router_api/resources/bitcoin/address/address.py">get_info</a>(address) -> None</code>
- <code title="get /bitcoin/address/{address}/utxo">client.bitcoin.address.<a href="./src/multichain/wallet/router_api/resources/bitcoin/address/address.py">get_utxos</a>(address) -> None</code>

### Txs

Methods:

- <code title="get /bitcoin/address/{address}/txs">client.bitcoin.address.txs.<a href="./src/multichain/wallet/router_api/resources/bitcoin/address/txs.py">get_all</a>(address) -> None</code>
- <code title="get /bitcoin/address/{address}/txs/chain">client.bitcoin.address.txs.<a href="./src/multichain/wallet/router_api/resources/bitcoin/address/txs.py">get_paginated</a>(address, \*\*<a href="src/multichain/wallet/router_api/types/bitcoin/address/tx_get_paginated_params.py">params</a>) -> None</code>

## Tx

Methods:

- <code title="post /bitcoin/tx/send">client.bitcoin.tx.<a href="./src/multichain/wallet/router_api/resources/bitcoin/tx.py">broadcast</a>(\*\*<a href="src/multichain/wallet/router_api/types/bitcoin/tx_broadcast_params.py">params</a>) -> None</code>
- <code title="post /bitcoin/tx/decode">client.bitcoin.tx.<a href="./src/multichain/wallet/router_api/resources/bitcoin/tx.py">decode</a>(\*\*<a href="src/multichain/wallet/router_api/types/bitcoin/tx_decode_params.py">params</a>) -> None</code>
- <code title="get /bitcoin/tx/{txid}">client.bitcoin.tx.<a href="./src/multichain/wallet/router_api/resources/bitcoin/tx.py">get_info</a>(txid) -> None</code>
- <code title="get /bitcoin/tx/{txid}/raw">client.bitcoin.tx.<a href="./src/multichain/wallet/router_api/resources/bitcoin/tx.py">get_raw</a>(txid, \*\*<a href="src/multichain/wallet/router_api/types/bitcoin/tx_get_raw_params.py">params</a>) -> None</code>
- <code title="get /bitcoin/tx/{txid}/hex">client.bitcoin.tx.<a href="./src/multichain/wallet/router_api/resources/bitcoin/tx.py">get_raw_hex</a>(txid) -> None</code>
- <code title="get /bitcoin/tx/{txid}/status">client.bitcoin.tx.<a href="./src/multichain/wallet/router_api/resources/bitcoin/tx.py">get_status</a>(txid) -> None</code>
- <code title="post /bitcoin/tx/test">client.bitcoin.tx.<a href="./src/multichain/wallet/router_api/resources/bitcoin/tx.py">test_mempool</a>(\*\*<a href="src/multichain/wallet/router_api/types/bitcoin/tx_test_mempool_params.py">params</a>) -> None</code>

## Block

Methods:

- <code title="get /bitcoin/block/best">client.bitcoin.block.<a href="./src/multichain/wallet/router_api/resources/bitcoin/block.py">get_best</a>() -> None</code>
- <code title="get /bitcoin/block/hash/{hash}">client.bitcoin.block.<a href="./src/multichain/wallet/router_api/resources/bitcoin/block.py">get_by_hash</a>(hash, \*\*<a href="src/multichain/wallet/router_api/types/bitcoin/block_get_by_hash_params.py">params</a>) -> None</code>
- <code title="get /bitcoin/block/height/{height}">client.bitcoin.block.<a href="./src/multichain/wallet/router_api/resources/bitcoin/block.py">get_by_height</a>(height) -> None</code>
- <code title="get /bitcoin/block/{hash}/header">client.bitcoin.block.<a href="./src/multichain/wallet/router_api/resources/bitcoin/block.py">get_header</a>(hash, \*\*<a href="src/multichain/wallet/router_api/types/bitcoin/block_get_header_params.py">params</a>) -> None</code>
- <code title="get /bitcoin/block/{hash}/stats">client.bitcoin.block.<a href="./src/multichain/wallet/router_api/resources/bitcoin/block.py">get_stats</a>(hash) -> None</code>
- <code title="get /bitcoin/block/tip">client.bitcoin.block.<a href="./src/multichain/wallet/router_api/resources/bitcoin/block.py">get_tip</a>() -> None</code>
- <code title="get /bitcoin/block/{hash}/txids">client.bitcoin.block.<a href="./src/multichain/wallet/router_api/resources/bitcoin/block.py">get_transaction_ids</a>(hash) -> None</code>
- <code title="get /bitcoin/block/{hash}/txs">client.bitcoin.block.<a href="./src/multichain/wallet/router_api/resources/bitcoin/block.py">get_transactions</a>(hash, \*\*<a href="src/multichain/wallet/router_api/types/bitcoin/block_get_transactions_params.py">params</a>) -> None</code>

## Mempool

Methods:

- <code title="get /bitcoin/mempool">client.bitcoin.mempool.<a href="./src/multichain/wallet/router_api/resources/bitcoin/mempool.py">get_info</a>() -> None</code>
- <code title="get /bitcoin/mempool/blocks">client.bitcoin.mempool.<a href="./src/multichain/wallet/router_api/resources/bitcoin/mempool.py">get_projected_blocks</a>() -> None</code>
- <code title="get /bitcoin/mempool/raw">client.bitcoin.mempool.<a href="./src/multichain/wallet/router_api/resources/bitcoin/mempool.py">get_raw</a>(\*\*<a href="src/multichain/wallet/router_api/types/bitcoin/mempool_get_raw_params.py">params</a>) -> None</code>

## Fees

Methods:

- <code title="get /bitcoin/fees/estimate">client.bitcoin.fees.<a href="./src/multichain/wallet/router_api/resources/bitcoin/fees.py">estimate</a>(\*\*<a href="src/multichain/wallet/router_api/types/bitcoin/fee_estimate_params.py">params</a>) -> None</code>
- <code title="get /bitcoin/fees">client.bitcoin.fees.<a href="./src/multichain/wallet/router_api/resources/bitcoin/fees.py">get_recommended</a>() -> None</code>
