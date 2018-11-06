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

# print()

# let's check balances of each one:
print(b.get_balance('John'))
print(b.get_balance('Jane'))
print(b.get_balance('Megan'))
print(b.get_balance('Chris'))
print(b.get_balance('Kevin'))

# list of pending transactions
print(f'Pending transactions: {b.pendingTransactions}')

# OUTPUT

# Blockchain:
#
# Timestamp: Tue Nov  6 22:43:23 2018
# Transactions: []
# Previous Hash: 0
# Hash: cc8eeacd5d2df0d43208792a0d74886ee6e609b2baf03a0c28d7f60c9d18aac3
# Nonce: 0
# Pending transactions: [From: John, To: Jane, Amount: 600, From: John, To: Megan, Amount: 700, From: John, To: Chris, Amount: 800]
# JOHN is worth -2100 cryptocoins
# JANE is worth 600 cryptocoins
# MEGAN is worth 700 cryptocoins
# CHRIS is worth 800 cryptocoins
# KEVIN is worth 100 cryptocoins
# Pending transactions: []
