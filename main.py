from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/41516fb7bf984a40bed346e3465c7639"))

print(w3.isConnected())

block_info = w3.eth.getBlock('latest')
print(block_info.number)
print(block_info.transactions[0])
# print(dir(block_info))

balance = w3.eth.getBalance("0xc341F250edbba5921F6491fAca4e16FE8b4CEd14")
print(balance)
convert_balance = w3.fromWei(balance, 'ether')
print(convert_balance)
transaction = w3.eth.getTransaction(block_info.transactions[0])
print(transaction.hash)

