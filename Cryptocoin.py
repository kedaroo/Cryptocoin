# Importing libraries
from hashlib import sha256 # for hash generation
from time import asctime # for timestamping

# Block class
class Block:

    # Class constructor
	def __init__(self, transactions, previousHash = ''):
		self.transactions = transactions
		self.previousHash = previousHash
		self.timestamp = asctime()
		self.nonce = 0
		self.hash = self.calculate_hash()

    # Human - readable representation of each block
	def __repr__(self):
		return f'\n\nTimestamp: {self.timestamp}\nTransactions: {self.transactions}\nPrevious Hash: {self.previousHash}\nHash: {self.hash}\nNonce: {self.nonce}'

    # calculating has for each new block
	def calculate_hash(self):
		return sha256(str((self.timestamp, self.transactions, self.previousHash, self.nonce)).encode('utf-8')).hexdigest()

    # to mine block of each set of transactions
	def mine_block(self, difficulty):
		while self.hash[0:difficulty] != ''.join('0' for i in range(difficulty)):
			self.nonce += 1
			self.hash = self.calculate_hash()
		return f'BLOCK MINED: {self.hash}'

# Blockchain class
class Blockchain:

    # class constructor
	def __init__(self):
		self.chain = [self.create_genesis_block()]
		self.difficulty = 7
		self.pendingTransactions = []
		self.miningReward = 100

    # representation of the blockchain
	def __repr__(self):
		dbc = ''
		for i in self.chain:
			dbc += repr(i)
		return dbc

    # adds the 1st block of the blockchain
	def create_genesis_block(self):
		return Block([], '0')

    # returns latest block in the chain
	def get_latest_block(self):
		return self.chain[len(self.chain) - 1]

    # creates transaction
	def create_transaction(self, transaction):
		self.pendingTransactions.append(transaction)

	def mine_pending_transactions(self, miningRewardAddress):

		rewardTx = Transaction(None, miningRewardAddress, self.miningReward)
		self.pendingTransactions.append(rewardTx)

		block = Block(self.pendingTransactions, self.get_latest_block().hash)
		block.mine_block(self.difficulty)
		# print(f'Block successfully mined!')
		self.chain.append(block)

		self.pendingTransactions = []

	def is_chain_valid(self):

		true = 'Chain is valid'
		false = 'Chain is invalid'

		for i in range(len(self.chain)):
			currentBlock = self.chain[i+1]
			previousBlock = self.chain[i]

			if currentBlock.hash != currentBlock.calculate_hash():
				return false

			if currentBlock.previousHash != previousBlock.hash:
				return false

			else:
				return true

	def get_balance(self, address):

		balance = 0

		for block in self.chain:
			for trans in block.transactions:
				if  trans.fromAddress == address:
					balance -= trans.amount

				if trans.toAddress == address:
					balance += trans.amount

		return f'{address.upper()} is worth {balance} cryptocoins'

class Transaction:

	def __init__(self, fromAddress, toAddress, amount):
		self.fromAddress = fromAddress
		self.toAddress = toAddress
		self.amount = amount

	def __repr__(self):
		return f'From: {self.fromAddress}, To: {self.toAddress}, Amount: {self.amount}'

# b = Blockchain()
# b.create_transaction(Transaction('kedar', 'kedar2', 200))
# b.mine_pending_transactions('miner')
# print(b)
