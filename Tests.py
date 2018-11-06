from Cryptocoin import *

# creating a blockchain
b = Blockchain()
print(f'Blockchain: {b}')

# adding transactions to the blockchain
b.create_transaction(Transaction('John', 'Jane', 600))
b.create_transaction(Transaction('John', 'Megan', 700))
b.create_transaction(Transaction('John', 'Chris', 800)) # because John is rich!
print(f'Pending transactions: {b.pendingTransactions}')

# there are 3 pending transactions which need to be mined
# Kevin is our miner
b.mine_pending_transactions('Kevin')

# let's check balances each one:
b.get_balance('John')
b.get_balance('Jane')
b.get_balance('Megan')
b.get_balance('Chris')
b.get_balance('Kevin')

# list of pending transactions
print(f'Pending transactions: {b.pendingTransactions}')
