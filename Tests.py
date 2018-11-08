from Cryptocoin import *

# creating a blockchain
b = Blockchain()
print(f'Blockchain: {b}')

# setting difficulty. By default set to 3
b.set_difficulty(5)

# adding transactions to the blockchain
b.create_transaction(Transaction('John', 'Jane', 600))
b.mine_pending_transactions('Kevin')
b.create_transaction(Transaction('John', 'Megan', 700))
b.mine_pending_transactions('Jade')
b.create_transaction(Transaction('John', 'Chris', 800))
b.mine_pending_transactions('John')
b.create_transaction(Transaction('John', 'Rock', 1600))
b.mine_pending_transactions('Megan')
b.create_transaction(Transaction('Jonas', 'Jane', 15600))
b.mine_pending_transactions('Kedar')
b.create_transaction(Transaction('Ricky', 'Jade', 6500))
b.mine_pending_transactions('Ricky')
b.create_transaction(Transaction('Johan', 'Jane', 6000))
b.mine_pending_transactions('Ben')
b.create_transaction(Transaction('Joquinn', 'Ben', 60120))
b.mine_pending_transactions('Kevin')

# printing chain again
print(f'Blockchain: {b}')

# let's check balances of each one:
print(b.get_balance('John'))
print(b.get_balance('Jane'))
print(b.get_balance('Megan'))
print(b.get_balance('Chris'))
print(b.get_balance('Kevin'))
print(b.get_balance('Joquinn'))
print(b.get_balance('Ben'))
print(b.get_balance('Johan'))
print(b.get_balance('Jade'))
print(b.get_balance('Rock'))
print(b.get_balance('Jonas'))
print(b.get_balance('Kedar'))
print(b.get_balance('Ricky'))


# list of pending transactions
print(f'Pending transactions: {b.pendingTransactions}')
